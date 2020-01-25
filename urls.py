from django.urls import path
from . import views

urlpatterns = [
    # [...]
    path('info', views.TypeList.as_view(), name='type_list'),
    path('details/<int:pk>', views.TypeDetail.as_view(), name='type_details'),
    path('create', views.TypeCreate.as_view(), name='type_create'),
    path('update/<int:pk>', views.TypeUpdate.as_view(), name='type_update'),
    path('delete/<int:pk>', views.TypeDelete.as_view(), name='type_delete'),
]
