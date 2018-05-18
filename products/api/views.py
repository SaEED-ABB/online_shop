from django.http import JsonResponse
from django.contrib.auth.models import User

from products.models import Product, SetProduct


def add_to_user_basket(request):
    user = request.user
    product = Product.objects.get(slug=request.POST.get('product_slug'))
    basket = user.baskets.get_or_create(paid=False)[0]
    set_product = SetProduct.objects.get_or_create(product=product, basket=basket)[0]

    set_product.counter += 1
    set_product.sum_price += set_product.product.price
    set_product.save()

    basket.total_price += set_product.product.price
    basket.save()

    return JsonResponse({'message': '{} successfully added to your basket {}.'.format(set_product.product.name, user.username)})


def remove_from_user_basket(request):
    user = request.user
    product_count = request.POST.get('product_count', '1')

    basket = user.baskets.get(paid=False)
    set_product = SetProduct.objects.get(product__slug=request.POST.get('product_slug'), basket=basket)

    if product_count == 'all' or int(product_count) >= set_product.counter:
        basket.total_price -= set_product.sum_price
        basket.save()
        set_product.delete()
    else:
        set_product.counter -= int(product_count)
        set_product.sum_price -= int(product_count) * set_product.product.price
        set_product.save()

        basket.total_price -= int(product_count) * set_product.product.price
        basket.save()

    return JsonResponse({'message': '{} successfully removed from your basket {}'.format(set_product.product.name, user.username)})
