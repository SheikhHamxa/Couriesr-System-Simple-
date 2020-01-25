from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Shipment


class ShipmentList(ListView):
    model = Shipment


class ShipmentDetail(DetailView):
    model = Shipment


class ShipmentCreate(CreateView):
    model = Shipment
    fields = ['ship_size', 'ship_id', 'ship_initial_address', 'ship_type', 'ship_price', 'ship_reach_address']
    success_url = reverse_lazy('shipment_list')


class ShipmentUpdate(UpdateView):
    model = Shipment
    fields = ['ship_size', 'ship_id', 'ship_initial_address', 'ship_type', 'ship_price', 'ship_reach_address']
    success_url = reverse_lazy('shipment_list')


class ShipmentDelete(DeleteView):
    model = Shipment
    success_url = reverse_lazy('shipment_list')
