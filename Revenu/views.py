from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, TemplateView, DeleteView, UpdateView
from .models import Revenu
from .forms import RevenuForm

"""
class AjouterRevenuView(LoginRequiredMixin, CreateView):
    model = Revenu
    form_class = RevenuForm
    template_name = 'Revenu/ajouter_revenu.html'
    success_url = reverse_lazy('liste_revenus')  # Redirection après l'ajout

    def form_valid(self, form):
        # Associer le revenu à l'utilisateur connecté
        form.instance.user = self.request.user
        return super().form_valid(form)


class ListeRevenusView(LoginRequiredMixin, ListView):
    model = Revenu
    template_name = 'Revenu/liste_revenus.html'
    context_object_name = 'revenus'  # Nom utilisé dans le template pour référencer les objets

    def get_queryset(self):
        # Filtrer les revenus pour n'afficher que ceux de l'utilisateur connecté
        return Revenu.objects.filter(user=self.request.user)
"""

class ListeRevenusView(LoginRequiredMixin, TemplateView):
    template_name = 'Revenu/liste_revenus.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Filtrer les revenus fixes et variables pour l'utilisateur connecté
        revenus_fixes = Revenu.objects.filter(user=self.request.user, category="Fixes")
        revenus_variables = Revenu.objects.filter(user=self.request.user, category="Variables")

        # Calcul des sous-totaux
        total_fixes = sum(revenu.amount for revenu in revenus_fixes)
        total_variables = sum(revenu.amount for revenu in revenus_variables)

        # Calcul du total global
        total_global = total_fixes + total_variables

        # Ajouter les données calculées au contexte
        context['revenus_fixes'] = revenus_fixes
        context['revenus_variables'] = revenus_variables
        context['total_fixes'] = total_fixes
        context['total_variables'] = total_variables
        context['total_global'] = total_global

        return context

class RevenuCreateView(LoginRequiredMixin, CreateView):
    model = Revenu
    fields = ['name', 'amount', 'category']
    template_name = 'Revenu/ajouter_revenu.html'
    success_url = reverse_lazy('liste_revenus')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RevenuUpdateView(LoginRequiredMixin, UpdateView):
    model = Revenu
    fields = ['name', 'amount', 'category']
    template_name = 'Revenu/ajouter_revenu.html'
    success_url = reverse_lazy('liste_revenus')

class RevenuDeleteView(LoginRequiredMixin, DeleteView):
    model = Revenu
    template_name = 'Revenu/revenu_confirm_delete.html'
    success_url = reverse_lazy('liste_revenus')