from django.urls import path

from . import views


app_name = 'products_api'


urlpatterns = [
    path('add_to_user_basket/', views.add_to_user_basket, name='add_to_user_basket'),
]