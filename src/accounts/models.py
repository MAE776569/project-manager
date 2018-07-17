from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from os import urandom
from django.utils.text import slugify
from os.path import splitext

class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_admin, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, is_admin=is_admin, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fileds):
        return self._create_user(email, password, True, **extra_fileds)

def user_directory_path(instance, filename):
    image_name, image_ext = splitext(filename)
    image_name += urandom(5).hex()
    return 'avatars/{0}/{1}{2}'.format(instance.slug, image_name, image_ext)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=False)
    slug = models.SlugField(blank=True)
    name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(blank=True, default=True)
    is_admin = models.BooleanField(blank=True, default=False)
    date_joined = models.DateField(blank=True, auto_now_add=True)
    avatar = models.ImageField(blank=True, verbose_name="Profile Picture",
        upload_to=user_directory_path, default="avatars/default-avatar-image.png")

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
                self.slug = slugify(self.name + urandom(5).hex())
            else:
                self.slug = slugify(urandom(5).hex())
        return super().save(*args, **kwargs)

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin
