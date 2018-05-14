from django.shortcuts import render, get_object_or_404
from django.shortcuts import reverse, redirect

from itertools import chain

from .models import Category, Product, Comment
from .forms import CommentForm


def index(request):
    category = Category.objects.get_or_create(name='all')
    return redirect(reverse('products:related_products_view', kwargs={'slug': category.slug, }))


def related_products_view(request, slug):
    category = get_object_or_404(Category, slug=slug)

    cat_ancestors = category.get_ancestors(include_self=True)  # for showing path of current category to root

    cat_descendants = category.get_descendants(include_self=True)  # for future traverse for related products
    related_products = []
    for cat in cat_descendants:
        if cat.is_leaf_node() and cat.related_products.count != 0:
            related_products = list(chain(related_products, cat.related_products.all()))

    return render(request, 'products/index.html', {'category': category,
                                                   'cat_parent': category.parent,
                                                   'cat_children': category.children.all(),
                                                   'related_products': related_products,
                                                   'cat_ancestors': cat_ancestors,
                                                                })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    comments = Comment.objects.filter(product=product).order_by('-publish_time')
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(reverse('users:login'))
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.product = product
            comment.save()

    form = CommentForm()
    return render(request, 'products/product_detail.html', {'product': product, 'comments': comments, 'form': form, 'next': product.get_absolute_url()})


def show_basket(request):
    basket = request.user.baskets.get(paid=False)
    return render(request, 'products/basket.html', {'basket': basket})


def pay_request(request):
    pass