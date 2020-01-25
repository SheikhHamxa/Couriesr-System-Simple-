from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse

# Create your views here.


from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Type


class TypeList(ListView):
    model = Type


class TypeDetail(DetailView):
    model = Type


class TypeCreate(CreateView):
    model = Type
    fields = ['name', 'type', 'user_type_id', ]
    success_url = reverse_lazy('type_list')


class TypeUpdate(UpdateView):
    model = Type
    fields = ['name', 'type', 'user_type_id', ]
    success_url = reverse_lazy('type_list')


class TypeDelete(DeleteView):
    model = Type
    success_url = reverse_lazy('type_list')
