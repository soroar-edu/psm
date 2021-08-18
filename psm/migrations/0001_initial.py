# Generated by Django 3.2 on 2021-08-18 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('category', models.IntegerField(blank=True, choices=[(1, 'Covid Medical Item'), (2, 'Covid Safety Item'), (3, 'Dengue/Chikungunya'), (4, 'Cholera')], null=True)),
                ('stock_quantity', models.IntegerField(blank=True, null=True)),
                ('used_quantity', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('distribution_type', models.IntegerField(blank=True, choices=[(1, 'Per Person'), (2, 'Percentage')], default=1, null=True)),
                ('distribution_amount', models.FloatField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('body', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('body', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RequestedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_body', models.IntegerField(blank=True, choices=[(1, 'National'), (2, 'NeighborDistrict')], default=1, null=True)),
                ('quantity', models.IntegerField()),
                ('status', models.IntegerField(blank=True, choices=[(1, 'Pending'), (2, 'Approved')], default=1, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requested_items', to='psm.district')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requested_items', to='psm.item')),
                ('request_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_items', to='psm.district')),
            ],
        ),
        migrations.CreateModel(
            name='NeighborDistrict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighbor_districts', to='psm.district')),
                ('neighbor_district', models.ManyToManyField(related_name='districts', to='psm.District')),
            ],
        ),
        migrations.CreateModel(
            name='DistrictUserPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='district_user_permissions', to='psm.district')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='district_user_permissions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DistrictStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_quantity', models.IntegerField(blank=True, null=True)),
                ('used_quantity', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district_stores', to='psm.district')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district_stores', to='psm.item')),
            ],
        ),
    ]
