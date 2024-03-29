from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from datetime import datetime

class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('Entrada')
    template_name = 'Central/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        hora = datetime.now().hour
        if 6 <= hora < 12:
            context['saudacao'] = "Bom dia!"
        elif 12 <= hora < 18:
            context['saudacao'] = "Boa tarde!"
        else:
            context['saudacao'] = "Boa noite!"

        return context
