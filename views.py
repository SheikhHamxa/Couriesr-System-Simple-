from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse

# Create your views here.


from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import User


class UserList(ListView):
    model = User


class UserDetail(DetailView):
    model = User


class UserCreate(CreateView):
    model = User
    fields = ['name', 'email', 'address', 'phone', 'cnic', 'office', 'reg_no', 'user_type_id']
    success_url = reverse_lazy('user_list')


class UserUpdate(UpdateView):
    model = User
    fields = ['name', 'email', 'address', 'phone', 'cnic', 'office', 'reg_no', 'user_type_id']
    success_url = reverse_lazy('user_list')


class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('user_list')
