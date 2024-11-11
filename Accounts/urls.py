from django.urls import path, include
from .views import Profile, CustomLogoutView, SignupView, ContactView, ContactSucces, CustomPasswordChangeView
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", include('django.contrib.auth.urls')),
    path("inscription/", SignupView.as_view(), name='signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path("profile/", Profile.as_view(), name='profile'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/success/', ContactSucces.as_view(), name='contact_success'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/',
         TemplateView.as_view(template_name='password_change_done.html'), name='password_change_done'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]
