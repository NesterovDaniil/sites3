from django.db import models
from django.contrib.auth.models import AbstractUser

from django.dispatch import Signal

from .utilities import send_activation_notification

user_registrated = Signal(providing_args=['instance'])


def user_registrated_dispatcher(sender, **kwargs):
    send_activation_notification()


user_registrated.connect(user_registrated_dispatcher)


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True)


#  СОЗДАНИЕ ЗАЯВКИ
# import the standard Django Model
# from built-in library
from django.db import models


# declare a new model with a name "GeeksModel"
#class GeeksModel(models.Model):
    # fields of the model
 #   title = models.CharField(max_length=200)
   # description = models.TextField()

    # renames the instances of the model
    # with their title name
   # def __str__(self):
     #   return self.title
