from django.core.paginator import Paginator
from django.shortcuts import render

from db_request_app.models import Order, Requisite


def order_listing(request):
    orders_list = Order.objects.all()
    paginator = Paginator(orders_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'orders.html', {'page_obj': page_obj})


def requisites(request):
    requisites_list = Requisite.objects.all()
    paginator = Paginator(requisites_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'requisites.html', {'page_obj': page_obj})


def index(request):
    return render(request, 'base.html')
