from django.contrib import admin
from django.contrib.auth.models import User

from .models import Category, Product, Basket, SetProduct


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug', 'publish_date', 'price')


class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'create_time', 'pay_time', 'paid')


class SetProductAdmin(admin.ModelAdmin):
    list_display = ('basket', 'product', 'counter', 'sum_price')

    actions = ['really_delete_selected']

    def get_actions(self, request):
        actions = super(SetProductAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            obj.basket.total_price -= obj.sum_price
            obj.basket.save()
            obj.delete()

        if queryset.count() == 1:
            message_bit = "1 set_product entry was"
        else:
            message_bit = "%s set_product entries were" % queryset.count()
        self.message_user(request, "%s successfully deleted." % message_bit)

    really_delete_selected.short_description = "Delete selected entries"


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
admin.site.register(SetProduct, SetProductAdmin)
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
