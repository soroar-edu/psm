from django.contrib import admin
from .models import District, DistrictUserPermission, Item, Notice, UserProfile, DistrictStore,NeighborDistrict,ResearchArticle,RequestedItem

# from api.admin import GenericModelAdmin
from django.contrib import admin


# from api import models


# class ItemInline(admin.TabularInline):
#     model = Item
#     # form = OrderFlavorInlineForm
#     extra = 1
#
#
# class CategoryAdmin(admin.ModelAdmin):
#     inlines = (ItemInline,)
#     list_display = (
#         'name', 'total_item')
#     search_fields = ('name',)


class DistrictStoreInline(admin.TabularInline):
    model = DistrictStore
    # form = OrderFlavorInlineForm
    extra = 1


class DistrictAdmin(admin.ModelAdmin):
    inlines = (DistrictStoreInline,)
    list_display = (
        'name',)
    search_fields = ('name',)


class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('name','category','stock_quantity','distribution_type','distribution_amount')


# Register your models here.

# admin.site.register(Category, CategoryAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(DistrictUserPermission)
admin.site.register(Item,ItemAdmin)
admin.site.register(Notice)
admin.site.register(UserProfile)
admin.site.register(NeighborDistrict)
admin.site.register(ResearchArticle)
admin.site.register(RequestedItem)
