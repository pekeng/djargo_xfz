#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from shortuuidfield import ShortUUIDField


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, telephone, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        if not telephone:
            raise ValueError('The given telephone must be set')
        if not password:
            raise ValueError('The given password must be set')
        user = self.model(username=username, telephone=telephone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, telephone=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, telephone, password, **extra_fields)

    def create_superuser(self, username, telephone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, telephone, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    uid = ShortUUIDField(primary_key=True, )
    telephone = models.CharField(max_length=11, unique=True)
    username = models.CharField(max_length=100, )
    email = models.EmailField(unique=True, )
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False, )
    is_active = models.BooleanField(default=True,)
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        full_name = '%s' % self.username
        return full_name.strip()

    def get_short_name(self):
        return self.username
