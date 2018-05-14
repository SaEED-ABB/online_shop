from django.urls import path

from . import views


app_name = 'products'


urlpatterns = [
    # path('request/', views.send_request, name='request'),
    # path('verify/', views.verify, name='verify'),

    path('related_products/<slug:slug>/', views.related_products_view, name='related_products_view'),
    path('product_detail/<slug:slug>/', views.product_detail, name='product_detail'),
    path('basket/', views.show_basket, name='show_basket'),
]