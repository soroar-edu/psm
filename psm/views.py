from django.shortcuts import render, HttpResponse
from .models import Item
from django.contrib.auth.decorators import login_required


# Create your views here.

def login(request):
    return render(request, 'login.html')


@login_required(login_url='/login')
def home(request):
    # print(request.user)
    return render(request, 'home.html')


@login_required(login_url='/login')
def category(request, id):
    district = request.user.district_user_permissions.first().district
    # print(id)
    if id == 1:
        context = {"district": district,
                   'category': id,
                   'hygenic_items': district.district_stores.filter(item__category=2),
                   'medical_items': district.district_stores.filter(item__category=1),
                   }
    if id == 3:
        context = {"district": district,
                   'category': id,
                   'dengu_items': district.district_stores.filter(item__category=3),

                   }
    if id == 4:
        context = {"district": district,
                   'category': id,
                   'cholera_items': district.district_stores.filter(item__category=4),

                   }
    # print(context)
    return render(request, 'category.html', context)


@login_required(login_url='/login')
def national_stock(request, id):
    if id == 1:
        context = {
            'category': id,
            'hygenic_items': Item.objects.filter(category=2),
            'medical_items': Item.objects.filter(category=1),
        }
    if id == 3:
        context = {
            'category': id,
            'dengu_items': Item.objects.filter(category=3),

        }
    if id == 4:
        context = {
            'category': id,
            'cholera_items': Item.objects.filter(category=4),

        }

    return render(request, 'national_stock.html', context)
