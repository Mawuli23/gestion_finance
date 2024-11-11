from .models import CustomUser

from django import forms
from django.utils.safestring import mark_safe

from django.contrib.auth.forms import UserCreationForm


class CustomSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "nom", "prenom_1", "prenom_2", "zip_code", "password1", "password2")

    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ajouter des placeholders pour chaque champ
        self.fields['zip_code'].widget.attrs.update({'placeholder': "Entrez votre code postal..."})
        self.fields['email'].widget.attrs.update({'placeholder': "Entrez votre adresse mail..."})
        self.fields['nom'].widget.attrs.update({'placeholder': "Entrez votre nom..."})
        self.fields['prenoms'].widget.attrs.update({'placeholder': "Entrez vos prenoms..."})
        self.fields['password1'].widget.attrs.update({'placeholder': "Choisissez un mot de passe..."})
        self.fields['password2'].widget.attrs.update({'placeholder': "Confirmez votre mot de passe..."})

        for field_name, field in self.fields.items():
            if field.required:
                field.label = mark_safe(f"{field.label} <span class='required'>*</span>")"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Ajouter des placeholders pour chaque champ
        placeholders = {
            'zip_code': "Entrez votre code postal...",
            'email': "Entrez votre adresse mail...",
            'nom': "Entrez votre nom...",
            'prenom_1': "Entrez vos prénoms...",
            'prenom_2': "Entrez vos prénoms...",
            'password1': "Choisissez un mot de passe...",
            'password2': "Confirmez votre mot de passe...",
        }

        for field_name, placeholder_text in placeholders.items():
            self.fields[field_name].widget.attrs.update({'placeholder': placeholder_text})

        self.fields['password1'].required = True
        self.fields['password2'].required = True

        # Ajouter l'astérisque aux champs requis
        for field_name, field in self.fields.items():
            if field.required:
                field.label = mark_safe(f"{field.label} <span class='required'>*</span>")


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nom ')
    email = forms.EmailField(label='E-mail ')
    objet = forms.CharField(max_length=100, label='Objet', required=False)
    message = forms.CharField(widget=forms.Textarea, label='Message ')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ajouter des placeholders pour chaque champ
        self.fields['name'].widget.attrs.update({'placeholder': "Entrez votre nom..."})
        self.fields['email'].widget.attrs.update({'placeholder': "Entrez votre adresse mail..."})
        self.fields['objet'].widget.attrs.update({'placeholder': "Entrez votre demande..."})
        self.fields['message'].widget.attrs.update({'placeholder': "Entrez votre message..."})

        for field_name, field in self.fields.items():
            if field.required:
                field.label = mark_safe(f"{field.label} <span class='required'>*</span>")
