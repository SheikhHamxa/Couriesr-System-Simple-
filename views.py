from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Sender

class SenderList(ListView):
    model = Sender


class SenderDetail(DetailView):
    model = Sender


class SenderCreate(CreateView):
    model = Sender
    fields = ['name', 'email', 'address', 'phone', 'cnic']
    success_url = reverse_lazy('sender_list')


class SenderUpdate(UpdateView):
    model = Sender
    fields = ['name', 'email', 'address', 'phone', 'cnic']
    success_url = reverse_lazy('sender_list')


class SenderDelete(DeleteView):
    model = Sender
    success_url = reverse_lazy('sender_list')
