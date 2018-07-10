from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from os import urandom
from django.utils.text import slugify

class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_admin, is_superuser, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, is_admin=is_admin,
                is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fileds):
        return self._create_user(email, password, True, True, **extra_fileds)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=False)
    slug = models.SlugField(blank=True)
    name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(blank=True, default=True)
    is_admin = models.BooleanField(blank=True, default=False)
    is_superuser = models.BooleanField(blank=True, default=False)
    date_joined = models.DateField(blank=True, auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            if self.name:
                self.slug = self.name + urandom(5).hex()
            else:
                self.slug = urandom(5).hex()
        return super().save(*args, **kwargs)
