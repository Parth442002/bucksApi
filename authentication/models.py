from django.contrib.gis.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import AccountManager
import uuid


class Account(AbstractBaseUser, PermissionsMixin):
    '''
    CustomAccount Model
    '''
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    primary_identifier = models.CharField(unique=True, max_length=200)
    email = models.EmailField(verbose_name="Email",
                              null=True, blank=True, unique=True, max_length=100)
    phone = models.CharField(max_length=50, unique=True, null=True, blank=True)
    fullname = models.CharField(
        max_length=150, unique=True, null=True, blank=True)

    # ⚠️⚠️
    location = models.PointField(blank=True, null=True)

    # Linked BankDetails-

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now_add=True)

    objects = AccountManager()

    USERNAME_FIELD = 'primary_identifier'

    def __str__(self):
        return self.primary_identifier
