from django.urls import path
from .views import ListeChargesView, ChargeCreateView, ChargeUpdateView, ChargeDeleteView

urlpatterns = [
    path('', ListeChargesView.as_view(), name='liste_charges'),
    path('ajouter/', ChargeCreateView.as_view(), name='ajouter_charge'),
    path('<int:pk>/modifier/', ChargeUpdateView.as_view(), name='modifier_charge'),
    path('<int:pk>/supprimer/', ChargeDeleteView.as_view(), name='supprimer_charge'),
]
