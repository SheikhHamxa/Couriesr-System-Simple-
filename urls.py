from django.urls import path
from . import views

urlpatterns = [
    # [...]
    path('system', views.SenderList.as_view(), name='sender_list'),
    path('details/<int:pk>', views.SenderDetail.as_view(), name='sender_details'),
    path('create', views.SenderCreate.as_view(), name='sender_create'),
    path('update/<int:pk>', views.SenderUpdate.as_view(), name='sender_update'),
    path('delete/<int:pk>', views.SenderDelete.as_view(), name='sender_delete'),
]
