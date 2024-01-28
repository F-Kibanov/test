from random import randint, choice
from django.core.management.base import BaseCommand
from db_request_app.models import Order, Requisite


class Command(BaseCommand):
    help = 'Fill requests db with fake data.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of fake user orders')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        order_status = ('pending', 'accepted', 'declined')
        for _ in range(count):
            order = Order(summ=randint(10_000, 20_000), requisite=Requisite.objects.order_by('?').first(),
                          status=choice(order_status))
            order.save()
            print(order)
