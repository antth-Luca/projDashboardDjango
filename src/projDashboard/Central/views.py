from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from datetime import datetime, timedelta
from .models import Cliente, Vendedor, Produto, Venda, Despesa
from django.db.models import Sum, Count
from django.utils import timezone
import json

class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('Entrada')
    template_name = 'Central/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Tratando todos os dados da página:
        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

        # -> Saudação
        hora = datetime.now().hour
        if 6 <= hora < 12:
            context['saudacao'] = "Bom dia!"
        elif 12 <= hora < 18:
            context['saudacao'] = "Boa tarde!"
        else:
            context['saudacao'] = "Boa noite!"

        # -> Mês atual
        context['mes_atual'] = meses[datetime.now().month - 1]

        # -> Total vendas
        context['tot_vendas'] = Venda.objects.aggregate(total_vendas=Sum('total'))['total_vendas'] or 0

        # -> Total despesas
        context['tot_despesas'] = Despesa.objects.aggregate(total_despesas=Sum('valor'))['total_despesas'] or 0

        # -> Lucro
        context['lucro'] = context['tot_vendas'] - context['tot_despesas']

        # -> Faturamento último ano
        meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        data = []
        labels = []
        today = timezone.now()
        for cont in range(12):
            start_date = today - timedelta(days=30*cont)
            end_date = today - timedelta(days=30*(cont-1))
            data.append(Venda.objects.filter(data__range=(start_date, end_date)).aggregate(total_vendas=Sum('total'))['total_vendas'] or 0)
            labels.append(meses[cont])
        context['faturamento'] = {'data': json.dumps(data), 'labels': json.dumps(labels)}

        # -> Top 5 vendedores
        dict_tops = {}
        month_start = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        month_end = month_start.replace(month=month_start.month % 12 + 1)
        list_tops = Venda.objects.filter(data__range=(month_start, month_end)).values('vendedor__nome').annotate(total_vendas=Sum('total')).order_by('-total_vendas')[:5]
        cont = 1
        for top in list_tops:
            dict_tops[cont] = top
            cont += 1
        context['top_vendedores'] = dict_tops

        # -> Top 5 produtos
        dict_tops = {}
        month_start = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        month_end = month_start.replace(month=month_start.month % 12 + 1)
        list_tops = Venda.objects.filter(data__range=(month_start, month_end)).values('produto__nome').annotate(total_vendas=Count('produto')).order_by('-total_vendas')[:5]
        cont = 1
        for top in list_tops:
            dict_tops[cont] = top
            cont += 1
        context['top_produtos'] = dict_tops

        # -> (%) de clientes que voltam comprar em 3 meses
        data_atual = timezone.now()
        tres_meses_atras = data_atual - timedelta(days=90)
        total_clientes = Cliente.objects.filter(
            venda__data__gte=tres_meses_atras,
            venda__data__lte=data_atual
        ).distinct().count()
        clientes_compra_recente = Cliente.objects.filter(
            venda__data__gte=tres_meses_atras,
            venda__data__lte=data_atual
        ).annotate(total_compras=Count('venda')).filter(total_compras__gte=2).count()
        context['porc_clientes_voltam'] = round((clientes_compra_recente / total_clientes) * 100 if total_clientes > 0 else 0, 1)

        # -> (%) de clientes que se cadastraram e compraram no mesmo mês num período de três meses atrás
        data_atual = timezone.now()
        three_months_ago = data_atual - timedelta(days=90)
        clientes_three_months_ago = Cliente.objects.filter(
            cadastro_em__gte=three_months_ago,
            cadastro_em__lte=data_atual
        ).distinct()

        total_novos_clientes = clientes_three_months_ago.count()  # Contagem correta dos novos clientes
        novos_clientes_compras = 0

        for cliente in clientes_three_months_ago:
            # Verifica se existe uma venda para o cliente no mesmo mês e ano do cadastro
            if Venda.objects.filter(cliente=cliente, data__year=cliente.cadastro_em.year, data__month=cliente.cadastro_em.month).exists():
                for cadastro in Venda.objects.filter(cliente=cliente, data__year=cliente.cadastro_em.year, data__month=cliente.cadastro_em.month):
                    novos_clientes_compras += 1
        context['porc_novos_clientes_que_compraram'] = round((novos_clientes_compras / total_novos_clientes) * 100 if total_novos_clientes > 0 else 0, 1)

        # -> Clientes cadastrados no mês atual
        context['clientes_cadastrados'] = Cliente.objects.filter(cadastro_em__month=timezone.now().month).count()

        # -> Clientes atendidos no mês atual
        context['clientes_atendidos'] = Cliente.objects.filter(cadastro_em__month=timezone.now().month, venda__isnull=False).distinct().count()

        # -> Clientes sem atendimento no mês atual
        context['clientes_n_atendid'] = Cliente.objects.filter(cadastro_em__month=timezone.now().month, venda__isnull=True).count()

        # Retornando todos os dados
        return context


def void_view(request):
    from django.shortcuts import redirect
    return redirect(reverse_lazy('Dashboard'))