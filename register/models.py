from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django.contrib.auth.password_validation import validate_password

import uuid
# Create your models here.


class CustomerManager(BaseUserManager):
    use_in_migrations = True

    def _create_customer(
            self,
            email,
            password,
            is_staff,
            is_superuser,
            **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        if not password:
            raise ValueError('The given password must be set')
        email = self.normalize_email(email)
        customer = self.model(email=email, is_staff=is_staff,
                              is_superuser=is_superuser, is_active=True,
                              date_joined=now, **extra_fields)

        validate_password(password)
        customer.set_password(password)
        customer.save(using=self._db)
        return customer

        def create_user(self, email, password=None, **extra_fields):
            return self._create_customer(
                email,
                password,
                False,
                False,
                **extra_fields)

        def create_superuser(self, email, password, **extra_fields):
            return self._create_customer(
                email,
                password,
                True,
                True,
                **extra_fields)


class Customer(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        unique=True,
        primary_key=True,
        default=uuid.uuid4)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    date_of_birth = models.DateField(null=True)
    is_staff = models.BooleanField(
        default=False,
        help_text='Designates whether the customer can log into this admin.')
    is_active = models.BooleanField(
        default=False,
        help_text='Designates whether this customer should be treated as active.')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    objects = CustomerManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email
