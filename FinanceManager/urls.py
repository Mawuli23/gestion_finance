"""
URL configuration for FinanceManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import HomeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("admin/", admin.site.urls),
    path('revenus/', include("Revenu.urls")),
    path('epargnes/', include("Epargne.urls")),
    path('charges/', include('Charge.urls')),
    path('bilan-financier/', include('Bilan.urls')),
    path('accounts/', include('Accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
