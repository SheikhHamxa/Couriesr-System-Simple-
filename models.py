from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse


class Shipment(models.Model):
    ship_size = models.CharField(max_length=100)
    ship_id = models.CharField(max_length=6)
    ship_initial_address = models.CharField(max_length=100)
    ship_type = models.CharField(max_length=100)
    ship_price = models.CharField(max_length=50)
    ship_reach_address = models.CharField(max_length=100)


def __str__(self):
    return self.name


def get_absolute_url(self):
    return reverse('shipment_update', kwargs={'pk': self.pk})
