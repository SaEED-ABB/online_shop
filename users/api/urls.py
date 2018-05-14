from django.urls import path

from . import views


app_name = 'users_api'


urlpatterns = [
    path('validate_username/', views.validate_username, name='validate_username'),
]