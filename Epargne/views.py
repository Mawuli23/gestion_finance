from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Epargne


"""
class EpargneListView(LoginRequiredMixin, ListView):
    model = Epargne
    template_name = 'Epargne/epargne_list.html'
    context_object_name = 'epargnes'

    def get_queryset(self):
        # Filtre les épargnes pour l'utilisateur connecté
        return Epargne.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Récupère et assure que les montants sont sous forme de nombre
        epargnes = self.get_queryset().values_list('amount', flat=True)
        total_epargne = sum(float(epargne) for epargne in epargnes if epargne is not None)

        context['total_epargne'] = total_epargne
        return context"""

"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calcul de la somme des montants d'épargne pour l'utilisateur connecté
        total_epargne = self.get_queryset().aggregate(total=sum('amount'))['total']
        context[
            'total_epargne'] = total_epargne if total_epargne is not None else 0  # Défaut à 0 si aucun enregistrement
        return context

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calculer la somme des montants pour l'utilisateur connecté
        epargnes = Epargne.objects.filter(user=self.request.user)
        total_epargne = sum(epargne.amount for epargne in epargnes)
        context[
            'total_epargne'] = total_epargne if total_epargne is not None else 0  # Défaut à 0 si aucun enregistrement
        return context



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Filtrer les charges par type
        epargnes = Epargne.objects.filter(user=self.request.user)


        # Calcul des sous-totaux et du total global
        epargne_total = sum(epargne.amount for epargne in epargnes)


        # Ajouter les données au contexte
        context['epargne_total'] = epargne_total

        return context"""

class EpargneCreateView(LoginRequiredMixin, CreateView):
    model = Epargne
    template_name = 'Epargne/epargne_form.html'
    fields = ['user', 'name', 'amount', 'category']
    success_url = reverse_lazy('liste_epargnes')

class EpargneUpdateView(LoginRequiredMixin, UpdateView):
    model = Epargne
    template_name = 'Epargne/epargne_form.html'
    fields = ['user', 'name', 'amount', 'category']
    success_url = reverse_lazy('liste_epargnes')

class EpargneDeleteView(LoginRequiredMixin, DeleteView):
    model = Epargne
    template_name = 'Epargne/epargne_confirm_delete.html'
    success_url = reverse_lazy('liste_epargnes')




class EpargneListView(LoginRequiredMixin, ListView):
    template_name = 'Epargne/epargne_liste_v1.html'

    def get_queryset(self):
        # Filtre les épargnes pour l'utilisateur connecté
        return Epargne.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Filtrer les revenus fixes et variables pour l'utilisateur connecté
        epargnes_mensuel = Epargne.objects.filter(user=self.request.user, category="Mensuels")
        epargnes_investissement = Epargne.objects.filter(user=self.request.user, category="Investissements")

        # Calcul des sous-totaux
        total_epargnes_mensuels = sum(revenu.amount for revenu in epargnes_mensuel)
        total_epargnes_investissements = sum(revenu.amount for revenu in epargnes_investissement)

        # Calcul du total global
        total_epargne = total_epargnes_mensuels + total_epargnes_investissements

        # Ajouter les données calculées au contexte
        context['epargnes_mensuel'] = epargnes_mensuel
        context['epargnes_investissement'] = epargnes_investissement
        context['total_epargnes_mensuels'] = total_epargnes_mensuels
        context['total_epargnes_investissements'] = total_epargnes_investissements
        context['total_epargne'] = total_epargne

        return context
