from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from .models import DistrictStore, District, Notice, ResearchArticle, RequestedItem
from .models import Item
from django.db.models import Q
from django.urls import reverse
from django.shortcuts import redirect


class DistrictStoreForm(forms.ModelForm):
    class Meta:
        model = DistrictStore
        fields = ('stock_quantity',)
        extra_kwargs = {
            'stock_quantity': {'required': False}
        }


# Create your views here.

class RequestedItemForm(forms.ModelForm):
    class Meta:
        model = RequestedItem
        fields = (
            'quantity',)


class RequestedStatusForm(forms.ModelForm):
    class Meta:
        model = RequestedItem
        fields = (
            'status',)


CATEGORY = ((1, 'Covid Medical Item'),
            (2, 'Covid Safety Item'),)


class CalculationForm(forms.Form):
    category = forms.ChoiceField(choices=CATEGORY)
    number_of_people = forms.FloatField()

    # class Meta:
    #     model = DistrictStore
    #     fields = (
    #         'item',
    #         'number_of_people'
    #     )


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
                   'neighbour_district': district,
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


@login_required(login_url='/login')
def notice(request, category_id):
    if category_id == 2:
        category_id = 1

    context = {
        "notice": Notice.objects.all(),
        "district": request.user.district_user_permissions.first().district,
        "category": category_id
    }
    return render(request, 'notice.html', context)


@login_required(login_url='/login')
def notice_details(request, category_id, id):
    if category_id == 2:
        category_id = 1

    context = {
        "notice": Notice.objects.filter(id=id).first(),
        "district": request.user.district_user_permissions.first().district,
        "category": category_id
    }
    return render(request, 'notice_details.html', context)


@login_required(login_url='/login')
def research_article(request, category_id):
    if category_id == 2:
        category_id = 1

    context = {
        "research_article": ResearchArticle.objects.all(),
        "district": request.user.district_user_permissions.first().district,
        "category": category_id
    }
    return render(request, 'research_article.html', context)


@login_required(login_url='/login')
def research_article_details(request, category_id, id):
    if category_id == 2:
        category_id = 1

    context = {
        "research_article": ResearchArticle.objects.filter(id=id).first(),
        "district": request.user.district_user_permissions.first().district,
        "category": category_id
    }
    return render(request, 'research_article_details.html', context)


def request_stock(request, category_id, id, district_id=None, quantity=None):
    district = request.user.district_user_permissions.first().district
    context = {}
    if request.method == "GET":
        item = Item.objects.get(id=id)
        request_item = RequestedItem(district=district, item=item, quantity=quantity)
        request_item.save()

    if category_id == 2:
        category_id = 1

    # pass the object as instance in form
    form = RequestedItemForm(request.POST or None, initial={'quantity': quantity})

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        request_item = form.save(commit=False)
        request_item.district = district
        if district_id:
            request_item.request_body = 2
            request_item.request_to = District.objects.get(id=district_id)
        request_item.item = Item.objects.get(id=id)
        request_item.save()
        # if quantity:
        #     next = request.POST.get('next', '/')
        #     return HttpResponseRedirect('/calculation_result/1')
        #     return redirect(request.META.get('HTTP_REFERER'))
        #     # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        #     # return HttpResponseRedirect("/national_stock/{}".format(category_id))
        return HttpResponseRedirect("/national_stock/{}".format(category_id))

    # add form dictionary to context
    context["form"] = form
    context["category"] = category_id
    context['district'] = district
    context['quantity'] = quantity

    return render(request, 'request_stock.html', context)


@login_required(login_url='/login')
def requested_stock(request, id):
    district = request.user.district_user_permissions.first().district
    if id == 1:
        context = {
            'category': id,
            'district': district,
            'hygenic_items': RequestedItem.objects.filter(item__category=2).filter(
                Q(district=district) | Q(request_to=district)),
            'medical_items': RequestedItem.objects.filter(
                Q(district=district, item__category=1) | Q(request_to=district, item__category=1)),
        }
    if id == 3:
        context = {
            'category': id,
            'district': district,
            'dengu_items': RequestedItem.objects.filter(item__category=3).filter(
                Q(district=district) | Q(requested_to=district)),

        }
    if id == 4:
        context = {
            'category': id,
            'district': district,
            'cholera_items': RequestedItem.objects.filter(item__category=4).filter(
                Q(district=district) | Q(request_to=district)),

        }

    return render(request, 'requested_stock_list.html', context)


def update_status(request, category_id, id):
    # book = get_object_or_404(Book, pk=pk)
    # if request.method == 'POST':
    #     form = BookForm(request.POST, instance=book)
    # else:
    #     form = BookForm(instance=book)
    district = request.user.district_user_permissions.first().district
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(RequestedItem, id=id)
    # category_id = obj.item.category
    if category_id == 2:
        category_id = 1

    # pass the object as instance in form
    form = RequestedStatusForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/requested_stock/{}".format(category_id))

    # add form dictionary to context
    context["form"] = form
    context["category"] = category_id
    context['district'] = district

    return render(request, 'update_status.html', context)


def calculation(request, category_id):
    district = request.user.district_user_permissions.first().district
    context = {}

    if category_id == 2:
        category_id = 1

    form = CalculationForm(request.POST or None)

    context["form"] = form
    context["category"] = category_id
    context['district'] = district

    return render(request, 'calculation.html', context)


def calculation_result(request, category_id):
    district = request.user.district_user_permissions.first().district
    context = {}

    # fetch the object related to passed id
    # obj = get_object_or_404(RequestedItem, id=id)
    # category_id = obj.item.category
    if category_id == 2:
        category_id = 1
    item_list = []
    if request.method == 'POST':
        category = int(request.POST['category'])
        items = Item.objects.filter(category=category)
        # print(type(category))
        # print(items)
        number_of_people = int(request.POST['number_of_people'])
        for item in items:
            distribution_type = item.distribution_type
            distribution_amount = item.distribution_amount
            if distribution_type == 1:
                calculated_amount = number_of_people * distribution_amount
            else:
                calculated_amount = int(round(number_of_people * distribution_amount / 100))
            if item.district_stores.first():
                stock_amount = item.district_stores.first().stock_quantity
            else:
                stock_amount = 0

            if stock_amount > calculated_amount:
                needed_amount = 0
            else:
                needed_amount = calculated_amount - stock_amount
            pending_amount = sum(item.requested_items.filter(status=1).values_list('quantity', flat=True))
            # print(pending_amount)
            if pending_amount+stock_amount >= calculated_amount:
                is_request = False
            else:
                is_request = True
            item_dict = {
                'id': item.id,
                'name': item.name,
                'image': item.image,
                'calculated_amount': int(calculated_amount),
                'stock_amount': stock_amount,
                'needed_amount': int(needed_amount),
                'is_request': is_request
            }

            item_list.append(item_dict)

        context["category"] = category_id
        context['district'] = district
        context['items'] = item_list
        context['number_of_people'] = number_of_people
        context['form'] = RequestedItemForm()
        # context['calculated_item'] = int(calculated_item)
        return render(request, 'calculation_result.html', context)
    return redirect(reverse('calculation', kwargs={'category_id': category_id}))
