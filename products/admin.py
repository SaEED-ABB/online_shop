from django.contrib import admin
from django.contrib.auth.models import User

from .models import Category, Product, Basket


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug', 'publish_date', 'cost')


class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'create_time', 'pay_time', 'paid')


# class BasketInlineAdmin(admin.TabularInline):
#     model = Basket
#     extra = 1
#
#
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'first_name', 'last_name', 'date_joined', 'email')
#     inlines = BasketInlineAdmin


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Basket, BasketAdmin)
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
