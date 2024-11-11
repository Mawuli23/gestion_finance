from django.urls import path, include
from .views import  ListeRevenusView, RevenuDeleteView, RevenuUpdateView, RevenuCreateView

urlpatterns = [
    path('ajouter/', RevenuCreateView.as_view(), name='ajouter_revenu'),
    path('revenus-list/', ListeRevenusView.as_view(), name='liste_revenus'),
    path('<int:pk>/modifier/', RevenuUpdateView.as_view(), name='modifier_revenu'),
    path('<int:pk>/supprimer/', RevenuDeleteView.as_view(), name='supprimer_revenu'),
]
