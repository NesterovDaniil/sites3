from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from django.dispatch import Signal

from .utilities import send_activation_notification

user_registrated = Signal(providing_args=['instance'])


def user_registrated_dispatcher(sender, **kwargs):
    send_activation_notification()


user_registrated.connect(user_registrated_dispatcher)


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True)


class Category(models.Model):
    name = models.CharField(max_length=200, help_text='Enter category)')

    def __str__(self):
        return self.name


class Order(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text='Описание')
    Category = models.ManyToManyField(Category, help_text='Выберете категорию')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])
