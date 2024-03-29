from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Category(models.Model):
#     name = models.CharField(max_length=120)
#     total_item = models.IntegerField(null=True, blank=True)
#
#     def save(self, *args, **kwargs):
#         self.total_item = self.get_total_item()
#
#         super(Category, self).save(*args, **kwargs)
#
#     def get_total_item(self):
#         return self.items.count()
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name_plural = "categories"

CATEGORY_TYPE = ((1, 'Covid Medical Item'),
                 (2, 'Covid Safety Item'),
                 (3, 'Dengue/Chikungunya'),
                 (4, 'Cholera'))

DISTRIBUTION_TYPE = ((1, 'Per Person'),
                     (2, 'Percentage'),)


class Item(models.Model):
    name = models.CharField(max_length=120)
    category = models.IntegerField(choices=CATEGORY_TYPE, null=True, blank=True)
    stock_quantity = models.IntegerField(null=True, blank=True)
    used_quantity = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    distribution_type = models.IntegerField(choices=DISTRIBUTION_TYPE, null=True, blank=True, default=1)
    distribution_amount = models.FloatField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Notice(models.Model):
    title = models.CharField(max_length=120)
    body = models.CharField(max_length=2000)
    file = models.FileField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title


class ResearchArticle(models.Model):
    title = models.CharField(max_length=120)
    body = models.CharField(max_length=2000)
    file = models.FileField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class DistrictUserPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='district_user_permissions', null=True,
                             blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='district_user_permissions',
                                 null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.district.name


class DistrictStore(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='district_stores')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='district_stores')
    stock_quantity = models.IntegerField(null=True, blank=True)
    used_quantity = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.district.name


class NeighborDistrict(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='neighbor_districts')
    neighbor_district = models.ManyToManyField(District, related_name='districts')


REQUEST_BODY = ((1, 'National'),
                (2, 'NeighborDistrict'))

STATUS = ((1, 'Pending'),
          (2, 'Approved'))


class RequestedItem(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='requested_items', blank=True,
                                 null=True)
    request_body = models.IntegerField(choices=REQUEST_BODY, default=1, blank=True, null=True)
    request_to = models.ForeignKey(District, on_delete=models.CASCADE, related_name='request_items', null=True,
                                   blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='requested_items', null=True, blank=True)
    quantity = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=1, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
