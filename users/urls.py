from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView,
)

from . import views


app_name = 'registration'


urlpatterns = [
    path('signup/', views.user_signup, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('ajax/validate_username/', views.validate_username, name='validate_username'),
]