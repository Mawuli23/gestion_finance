from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, nom, password=None):
        if not (email and nom):
            raise ValueError("Un Email est obligatoire")
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, nom, password=None):
        user = self.create_user(email=email, nom=nom, password=password)
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        unique=True,
        max_length=255,
        blank=False
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    nom = models.CharField(max_length=255)
    prenom_1 = models.CharField(blank=True, max_length=255)
    prenom_2 = models.CharField(blank=True, max_length=255)
    zip_code = models.CharField(blank=True, max_length=5, verbose_name="Code Postal")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nom"]

    objects = MyUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

