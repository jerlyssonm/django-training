import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Estamos modificando o comportamento da função que 
    faz a criação de usuários, para que os usuários sejam 
    criados com email e senha.
    """
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        now =timezone.now()

        if not email:
            raise ValueError('The given email mist be set')

        email = self.normalize_email(email)

        user = self.model(email=email, is_staff=is_staff, is_active=True,
                            is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user
        
    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)

class MyUser(AbstractUser):
    birthday_date = models.DateField()
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(unique=False, null=True, max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['birthday_date',]

    objects = CustomUserManager()
