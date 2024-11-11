from django.urls import path
from .views import EpargneListView, EpargneCreateView, EpargneUpdateView, EpargneDeleteView

urlpatterns = [
    path('epargnes/', EpargneListView.as_view(), name='liste_epargnes'),
    path('ajouter/', EpargneCreateView.as_view(), name='ajouter_epargne'),
    path('<int:pk>/modifier/', EpargneUpdateView.as_view(), name='modifier_epargne'),
    path('<int:pk>/supprimer/', EpargneDeleteView.as_view(), name='supprimer_epargne'),
]
