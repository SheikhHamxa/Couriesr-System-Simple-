from django.db import models

# Create your models here.


from django.urls import reverse


class Type(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    user_type_id = models.CharField(max_length=100)


def __str__(self):
    return self.name


def get_absolute_url(self):
    return reverse('type_update', kwargs={'pk': self.pk})
