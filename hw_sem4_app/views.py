import os.path
from datetime import datetime, timedelta

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

from .forms import GoodForm
from .models import Client, Good, Order

# Create your views here.
def shop_main(request):
    context = {'title': 'main'}
    return render(request,'hw_sem4_app/shop_main.html', context=context)


def find_date_for_filter(days: int):
    end = datetime.today()
    delta_sec = days * 24 * 60 * 60
    return (end - timedelta(seconds=delta_sec)).date()


def sort_orders_of_the_client_by_date_and_distinct_products(request, client_id: int, days: int):
    client = Client.objects.filter(id=client_id).first()
    number_of_clients = len(list(Client.objects.all()))
    sales_ = []
    orders_ = Order.objects.filter(
        order_client_id=client_id,
        order_date__gte=find_date_for_filter(days))
    good_set = set()
    for order in list(orders_):
        order_items = list(order.order_items.all())
        for good in order_items:
            if good not in good_set:
                sale = {'Товар': good.good_name,
                        'Номер заказа': order.id,
                        'Дата заказа': order.order_date}
                sales_.append(sale)
            good_set.add(good)
    sales = sorted(sales_, key=lambda x: x['Дата заказа'], reverse=True)
    context = {'title': f'{days} sales report',
               'sales': sales,
               'number_of_clients': number_of_clients,
               'days': days,
               'client': client.client_name}
    return render(request,'hw_sem4_app/shop_sales_report.html', context=context)


def add_good(request):
    if request.method == 'POST':
        form = GoodForm(request.POST, request.FILES)
        if form.is_valid():
            good_name = form.cleaned_data['good_name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            add_date = form.cleaned_data['add_date']
            image = form.cleaned_data['image']
            good = Good.objects.create(
                    good_name=good_name,
                    description=description,
                    price= price,
                    quantity=quantity,
                    add_date=add_date,
                )
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = GoodForm()
    context = {'title': 'Добавить товар', 'form': form}
    return render(request, 'hw_sem4_app/shop_add_good.html', context)


def add_good_with_pic_in_db(request):
    if request.method == 'POST':
        form = GoodForm(request.POST, request.FILES)
        if form.is_valid():
            good_name = form.cleaned_data['good_name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            add_date = form.cleaned_data['add_date']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            Good.objects.create(
                good_name=good_name,
                description=description,
                price=price,
                quantity=quantity,
                add_date=add_date,
                image=image
            )
    else:
        form = GoodForm()
    context = {'title': 'Добавить товар', 'form': form}
    return render(request, 'hw_sem4_app/shop_add_good.html', context)
