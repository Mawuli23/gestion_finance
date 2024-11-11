from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.edit import FormView

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from django.contrib.auth.views import LogoutView, TemplateView, PasswordChangeView
from django.contrib import messages

from django.core.mail import send_mail

# Create your views here.
from .forms import ContactForm

from .forms import CustomSignupForm  # Assurez-vous d'importer votre formulaire
from django.contrib.auth import get_user_model


class SignupView(FormView):
    template_name = "accounts/signup.html"
    form_class = CustomSignupForm
    success_url = reverse_lazy('home')  # Remplacez 'success' par le nom de votre URL de succès

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class Profile(LoginView):
    template_name = 'registration/login.html'  # Le template que vous utiliserez pour le formulaire de connexion
    redirect_authenticated_user = True  # Redirige l'utilisateur s'il est déjà authentifié
    success_url = reverse_lazy('home')  # Redirige après la connexion réussie

    # Si vous souhaitez rediriger vers une page spécifique après la connexion
    def get_success_url(self):
        return self.success_url


class CustomLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        messages.info(request, "Vous êtes déconnecté.")  # Message de déconnexion
        return super().post(request, *args, **kwargs)


class ContactView(FormView):
    template_name = "accounts/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')  # Redirige vers la page de succès

    def form_valid(self, form):
        # Logique de traitement du formulaire
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        objet = form.cleaned_data['objet']
        message = form.cleaned_data['message']

        message_to_send = message + '\n' + email

        send_mail(
            subject=f"Message de {name} - {objet} via le formulaire de contact",
            message=message_to_send,
            from_email=email,
            recipient_list=['skm.senyo@gmail.com'],  # Remplacez par votre email d'administration
            fail_silently=False,
        )

        return super().form_valid(form)

        # Vous pouvez ajouter ici du code pour envoyer un email ou enregistrer le message
        # Pour cet exemple, on retourne une simple réponse
        #print(f"Message de {name} ({email}): {message}")  # Pour débogage
        #return HttpResponse("Merci pour votre message !")


class ContactSucces(TemplateView):
    template_name = 'accounts/contactsucces.html'


class CustomPasswordChangeView(PasswordChangeView):
    model = get_user_model()  # Utilise le modèle d'utilisateur personnalisé
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('password_change_done')

    def form_valid(self, form):
        messages.success(self.request, 'Votre mot de passe a été mis à jour avec succès.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Veuillez corriger les erreurs ci-dessous.')
        return super().form_invalid(form)




