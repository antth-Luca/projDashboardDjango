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

        # -> Top 5 vendedores  #TODO: Verificar! Não está retornando os 3 resultados que deveria
        dict_tops = {}
        month_start = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        month_end = month_start.replace(month=month_start.month % 12 + 1)
        list_tops = Venda.objects.filter(data__range=(month_start, month_end)).values('vendedor__nome').annotate(total_vendas=Sum('total')).order_by('-total_vendas')[:5]
        cont = 1
        for top in list_tops:
            dict_tops[cont] = top
            cont += 1
        context['top_vendedores'] = dict_tops

        # -> Top 5 produtos  #TODO: Verificar! Não está retornando os 4 resultados que deveria
        dict_tops = {}
        month_start = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        month_end = month_start.replace(month=month_start.month % 12 + 1)
        list_tops = Venda.objects.filter(data__range=(month_start, month_end)).values('produto__nome').annotate(total_vendas=Count('produto')).order_by('-total_vendas')[:5]
        cont = 1
        for top in list_tops:
            dict_tops[cont] = top
            cont += 1
        context['top_produtos'] = dict_tops

        # -> (%) de clientes que voltam comprar em 3 meses  #TODO: Adicionar restrição: "total_clientes" e "clientes_recorrentes" devem buscar clientes que compraram até 3 meses atrás
        total_clientes = Cliente.objects.count()
        clientes_recorrentes = Cliente.objects.annotate(total_compras=Count('venda')).filter(total_compras__gte=2).count()
        context['porc_clientes_voltam'] = (clientes_recorrentes / total_clientes) * 100 if total_clientes > 0 else 0

        # -> (%) de clientes que se cadastraram e compraram no mesmo mês num período de três meses atrás  #TODO: Adicionar um range de hoje até 3 meses atrás
        three_months_ago = timezone.now() - timedelta(days=90)
        total_novos_clientes = Cliente.objects.filter(cadastro_em__gte=three_months_ago).count()
        novos_clientes_compras = Cliente.objects.filter(cadastro_em__gte=three_months_ago, venda__data__month=timezone.now().month).count()
        context['porc_novos_clientes_que_compraram'] = (novos_clientes_compras / total_novos_clientes) * 100 if total_novos_clientes > 0 else 0

        # -> Clientes cadastrados no mês atual
        context['clientes_cadastrados'] = Cliente.objects.filter(cadastro_em__month=timezone.now().month).count()

        # -> Clientes atendidos no mês atual  #TODO: Não contar duas vezes o mesmo cliente
        context['clientes_atendidos'] = Cliente.objects.filter(cadastro_em__month=timezone.now().month, venda__isnull=False).count()

        # -> Clientes sem atendimento no mês atual
        context['clientes_n_atendid'] = Cliente.objects.filter(cadastro_em__month=timezone.now().month, venda__isnull=True).count()

        # Retornando todos os dados
        return context


def void_view(request):
    from django.shortcuts import redirect
    return redirect(reverse_lazy('Dashboard'))