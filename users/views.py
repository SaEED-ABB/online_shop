from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.http import JsonResponse

from .forms import UserSignupFrom
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
            return redirect(reverse('products:related_products_view', kwargs={'slug': 'all'}))
    form = UserSignupFrom()
    return render(request, 'registration/user_signup.html', {'form': form, })


def validate_username(request):
    username = request.GET.get('username')
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists(),
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)
