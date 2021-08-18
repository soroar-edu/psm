from django.db.models.signals import post_save, post_delete
from psm.models import RequestedItem, Item, DistrictStore
from django.dispatch import receiver


@receiver(post_save, sender=RequestedItem)
@receiver(post_delete, sender=RequestedItem)
def update_purchase_store_contact(sender, instance, created=None, *args, **kwargs):
    if instance.status == 2:
        if instance.request_body == 1:
            item = Item.objects.get(id=instance.item.id)
            item.stock_quantity -= instance.quantity
            item.save()
        else:
            district_store = DistrictStore.objects.filter(district=instance.request_to).first()
            district_store.stock_quantity -= instance.quantity
            district_store.save()
        district_store = DistrictStore.objects.filter(district=instance.district).first()
        district_store.stock_quantity += instance.quantity
        district_store.save()
