from django.db import models

# Create your models here.


from django.urls import reverse


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    cnic = models.CharField(max_length=50)
    office = models.CharField(max_length=50)
    reg_no = models.CharField(max_length=50)
    user_type_id = models.CharField(max_length=50)


def __str__(self):
    return self.name


def get_absolute_url(self):
    return reverse('user_update', kwargs={'pk': self.pk})
