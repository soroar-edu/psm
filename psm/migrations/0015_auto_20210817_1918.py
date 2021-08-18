# Generated by Django 3.2 on 2021-08-17 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psm', '0014_requesteditem_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='distribution_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='distribution_type',
            field=models.IntegerField(blank=True, choices=[(1, 'Per Person'), (2, 'Percentage')], default=1, null=True),
        ),
    ]