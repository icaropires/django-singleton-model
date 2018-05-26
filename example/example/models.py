from django.db import models
from singleton_model import SingletonModel


class ConcreteSingleModel(SingletonModel):

    attr = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )
