from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import login
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, login, authenticate, logout
from django.contrib.auth.hashers import make_password

from .forms import UserSignupFrom, UserChangePasswordForm, UserLoginForm
from products.models import Basket


def user_signup(request):
    if request.method == 'POST':
        form = UserSignupFrom(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Basket.objects.create(user=new_user)
            login(request, new_user)
            messages.success(request, "You successfully registered!")

            return redirect(reverse('products:related_products_view', kwargs={'slug': 'all'}))
    form = UserSignupFrom()
    return render(request, 'users/user_signup.html', {'form': form, })


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "You successfully logged in!")
                return redirect('/')
            else:
                messages.error(request, "Wrong username or password supplied!")
    form = UserLoginForm()
    return render(request, 'users/user_login.html', {'form': form, })


def user_logout(request):
    logout(request)
    messages.success(request, "You logged out successfully!")
    return redirect('/')


def change_password(request):
    if request.method == 'POST':
        form = UserChangePasswordForm(data=request.POST)
        if form.is_valid():
            this_user = request.user
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            new_password_confirm = form.cleaned_data['new_password_confirm']

            if new_password == new_password_confirm:
                if this_user.check_password(old_password):
                    this_user.password = make_password(new_password)
                    this_user.save()
                    update_session_auth_hash(request, this_user)
                    messages.success(request, "Your password changed successfully!")
                    return redirect('/')
                else:
                    messages.error(request, "Incorrect password supplied. Try again please!")
            else:
                messages.error(request, 'New password confirm does not match!')

    form = UserChangePasswordForm()
    return render(request, 'users/change_password.html', {'form': form, })
