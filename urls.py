from django.urls import path
from . import views

urlpatterns = [
    # [...]
    path('info', views.ShipmentList.as_view(), name='shipment_list'),
    path('details/<int:pk>', views.ShipmentDetail.as_view(), name='shipment_details'),
    path('create', views.ShipmentCreate.as_view(), name='shipment_create'),
    path('update/<int:pk>', views.ShipmentUpdate.as_view(), name='shipment_update'),
    path('delete/<int:pk>', views.ShipmentDelete.as_view(), name='shipment_delete'),
]
