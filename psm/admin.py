from django.contrib import admin
from .models import District, DistrictUserPermission, Item, Notice, UserProfile, DistrictStore, NeighborDistrict, \
    ResearchArticle, RequestedItem
from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple


class NeighborDistrictForm(forms.ModelForm):
    neighbor_district = forms.ModelMultipleChoiceField(
        label="Neighbor District",
        queryset=District.objects.all(),
        widget=FilteredSelectMultiple('neighbor_district',
                                      False))

    class Meta:
        model = NeighborDistrict
        fields = [
            'district',
            'neighbor_district',

        ]


class NoticeForm(forms.ModelForm):
    body = forms.CharField(
        label="Notice Body",
        # help_text="diner notes",
        required=False,
        widget=forms.Textarea(
            attrs={'cols': '90', 'rows': '10'},

        )
    )

    class Meta:
        model = Notice
        fields = [
            'title',
            'body',
            'file'

        ]


class ResearchArticleForm(forms.ModelForm):
    body = forms.CharField(
        label="Research Article Body",
        # help_text="diner notes",
        required=False,
        widget=forms.Textarea(
            attrs={'cols': '90', 'rows': '10'},

        )
    )

    class Meta:
        model = ResearchArticle
        fields = [
            'title',
            'body',
            'file']


class NeighborDistrictAdmin(admin.ModelAdmin):
    form = NeighborDistrictForm

    @staticmethod
    def neighbor_district_name(obj):
        return list(obj.neighbor_district.all())

    list_display = ['district', 'neighbor_district_name']
    search_fields = ('district',)


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
    list_display = ('name', 'category', 'stock_quantity', 'distribution_type', 'distribution_amount')
    search_fields = ('name',)
    list_filter = ('category',)


class DistrictUserPermissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'district',)
    search_fields = ('district',)


class RequestedItemAdmin(admin.ModelAdmin):
    list_display = ('district', 'request_body', 'request_to', 'item', 'quantity', 'status')
    search_fields = ('district',)
    list_filter = ('request_body', 'status')


class NoticeAdmin(admin.ModelAdmin):
    form = NoticeForm
    list_display = ('title',)


class ResearchArticleAdmin(admin.ModelAdmin):
    form = ResearchArticleForm
    list_display = ('title',)


# Register your models here.

# admin.site.register(Category, CategoryAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(DistrictUserPermission, DistrictUserPermissionAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(UserProfile)
admin.site.register(NeighborDistrict, NeighborDistrictAdmin)
admin.site.register(ResearchArticle,ResearchArticleAdmin)
admin.site.register(RequestedItem, RequestedItemAdmin)
