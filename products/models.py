from django.db import models
from django.core.validators import validate_comma_separated_integer_list
from django.utils.text import slugify
from django.shortcuts import reverse
from django.contrib.auth.models import User

from mptt.models import TreeForeignKey, MPTTModel
from auto_posting.helpers import send_product


class Category(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True, db_index=True)
    slug = models.SlugField(unique=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:related_products_view', kwargs={'slug': self.slug})

    def __str__(self):
        full_name = []
        curr_categ = self
        while curr_categ is not None:
            full_name.append(curr_categ.name)
            curr_categ = curr_categ.parent
        full_name = ' -> '.join(reversed(full_name))
        return full_name


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='related_products')
    slug = models.SlugField(unique=True, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField(default=0)
    text_info = models.TextField(max_length=10000, blank=True)

    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, upload_to='product_images', height_field='height', width_field='width')

    on_telegram = models.BooleanField(default=True)

    def _get_unique_slug(self):
        slug = slugify(self.name)
        counter = 1
        while Product.objects.filter(slug=slug).exists():
            slug = '{}-{}'.format(slug, counter)
            counter += 1
        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        # super().save()
        limit = 150
        if self.width > self.height:
            self.height = int(self.height * limit / self.width)
            self.width = limit
        else:
            self.width = int(self.width * limit / self.height)
            self.height = limit
        save_result = super(Product, self).save(*args, **kwargs)
        if self.on_telegram:
            send_product.send_product(pro_obj=self)
        return save_result

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Comment(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=1023)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='related_products')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    publish_time = models.DateTimeField(auto_now_add=True)
    allow_publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='baskets')
    create_time = models.DateTimeField(auto_now_add=True)
    pay_time = models.DateTimeField(blank=True, null=True)
    total_price = models.PositiveIntegerField(default=0)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return 'basket for {}'.format(self.user.username)


class SetProduct(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='set_products')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='set_product')
    counter = models.PositiveIntegerField(default=0)
    sum_price = models.PositiveIntegerField(default=0)

    def delete(self, *args, **kwargs):
        self.basket.total_price -= self.sum_price
        self.basket.save()
        return super(SetProduct, self).delete(*args, **kwargs)

    def __str__(self):
        return '{} * {}'.format(self.counter, self.product)