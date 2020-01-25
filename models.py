from django.db import models
from django.urls import reverse


class Sender(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    cnic = models.DecimalField(max_digits=13, decimal_places=00000-0000000-0)


def __str__(self):
    return self.name


def get_absolute_url(self):
    return reverse('sender_update', kwargs={'pk': self.pk})
