from django.urls import path
from .views import user_list, user_register

urlpatterns = [
    path('users/', user_list),        # GET список пользователей
    path('users/register/', user_register),  # POST регистрация
]
