from django.urls import path
from .views import BilanFinancierView

urlpatterns = [
    path('bilan/', BilanFinancierView.as_view(), name='bilan_financier'),
]