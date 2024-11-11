from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Charge
from django.contrib.auth.mixins import LoginRequiredMixin



class ListeChargesView(LoginRequiredMixin, TemplateView):
    template_name = 'Charge/liste_charges.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Filtrer les charges par type
        charges_fixes = Charge.objects.filter(user=self.request.user, category="Fixes")
        charges_variables = Charge.objects.filter(user=self.request.user, category="Variables")

        # Calcul des sous-totaux et du total global
        total_fixes = sum(charge.amount for charge in charges_fixes)
        total_variables = sum(charge.amount for charge in charges_variables)
        total_global = total_fixes + total_variables

        # Ajouter les données au contexte
        context['charges_fixes'] = charges_fixes
        context['charges_variables'] = charges_variables
        context['total_fixes'] = total_fixes
        context['total_variables'] = total_variables
        context['total_global'] = total_global

        return context


class ChargeCreateView(LoginRequiredMixin, CreateView):
    model = Charge
    fields = ['name', 'amount', 'category']
    template_name = 'Charge/charge_form.html'
    success_url = reverse_lazy('liste_charges')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ChargeUpdateView(LoginRequiredMixin, UpdateView):
    model = Charge
    fields = ['name', 'amount', 'category']
    template_name = 'Charge/charge_form.html'
    success_url = reverse_lazy('liste_charges')

class ChargeDeleteView(LoginRequiredMixin, DeleteView):
    model = Charge
    template_name = 'Charge/charge_confirm_delete.html'
    success_url = reverse_lazy('liste_charges')
