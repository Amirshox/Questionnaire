from django.contrib.auth.models import AbstractUser, UserManager

from django.db import models


class MyUserManager(UserManager):
    def get_queryset(self):
        return super(MyUserManager, self).get_queryset().filter(is_active=True)


class User(AbstractUser):
    rating = models.PositiveIntegerField(default=0)

    objects = MyUserManager()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.username
