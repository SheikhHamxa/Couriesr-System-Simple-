from django.urls import path
from . import views

urlpatterns = [
    # [...]
    path('info', views.UserList.as_view(), name='user_list'),
    path('details/<int:pk>', views.UserDetail.as_view(), name='user_details'),
    path('create', views.UserCreate.as_view(), name='user_create'),
    path('update/<int:pk>', views.UserUpdate.as_view(), name='user_update'),
    path('delete/<int:pk>', views.UserDelete.as_view(), name='user_delete'),
]
