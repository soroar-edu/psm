from django.shortcuts import render, HttpResponse
from .models import Item
from django.contrib.auth.decorators import login_required
from django import forms
from .models import DistrictStore, District
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)


class DistrictStoreForm(forms.ModelForm):
    class Meta:
        model = DistrictStore
        fields = ('stock_quantity',)


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
    elif id == 3:
        context = {"district": district,
                   'category': id,
                   'dengu_items': district.district_stores.filter(item__category=3),

                   }
    elif id == 4:
        context = {"district": district,
                   'category': id,
                   'cholera_items': district.district_stores.filter(item__category=4),

                   }
    # print(context)
    else:
        context = {
            'category': id
        }

    return render(request, 'category.html', context)


@login_required(login_url='/login')
def national_stock(request, id):
    district = request.user.district_user_permissions.first().district
    if id == 1:
        context = {
            'category': id,
            'district': district,
            'hygenic_items': Item.objects.filter(category=2),
            'medical_items': Item.objects.filter(category=1),
        }
    if id == 3:
        context = {
            'category': id,
            'district': district,
            'dengu_items': Item.objects.filter(category=3),

        }
    if id == 4:
        context = {
            'category': id,
            'district': district,
            'cholera_items': Item.objects.filter(category=4),

        }

    return render(request, 'national_stock.html', context)


def update_stock(request, id):
    # book = get_object_or_404(Book, pk=pk)
    # if request.method == 'POST':
    #     form = BookForm(request.POST, instance=book)
    # else:
    #     form = BookForm(instance=book)
    district = request.user.district_user_permissions.first().district
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(DistrictStore, id=id)
    category_id = obj.item.category
    if category_id == 2:
        category_id = 1

    # pass the object as instance in form
    form = DistrictStoreForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/category/{}".format(category_id))

    # add form dictionary to context
    context["form"] = form
    context["category"] = category_id
    context['district'] = district

    return render(request, 'update_stock.html', context)


@login_required(login_url='/login')
def adjacent_district(request, district_id, id):
    district = District.objects.get(id=district_id)
    user_district = request.user.district_user_permissions.first().district
    # print(id)
    if id == 1:
        context = {"district": user_district,
                   'neighbour_district':district,
                   'category': id,
                   'hygenic_items': district.district_stores.filter(item__category=2),
                   'medical_items': district.district_stores.filter(item__category=1),
                   }
    elif id == 3:
        context = {"district": user_district,
                   'neighbour_district': district,
                   'category': id,
                   'dengu_items': district.district_stores.filter(item__category=3),

                   }
    elif id == 4:
        context = {"district": user_district,
                   'neighbour_district': district,
                   'category': id,
                   'cholera_items': district.district_stores.filter(item__category=4),

                   }
    # print(context)
    else:
        context = {
            'category': id,
            'district': user_district,
            'neighbour_district': district,
        }

    return render(request, 'adjacent_district.html', context)
