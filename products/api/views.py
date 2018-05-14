from django.http import JsonResponse
from django.contrib.auth.models import User

from products.models import Product


def add_to_user_basket(request):
    user = User.objects.get(username=request.POST.get('user_username'))
    product = Product.objects.get(slug=request.POST.get('product_slug'))

    basket = user.baskets.get_or_create(paid=False)[0]
    basket.products.add(product)
    basket.total_cost += product.cost
    basket.save()

    return JsonResponse({'message': '{} successfully added to your basket {}.'.format(product.name, user.username)})
