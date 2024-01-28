from random import randint, choice
from django.core.management.base import BaseCommand
# from elizabeth import Personal
from db_request_app.models import Requisite


class Command(BaseCommand):
    help = 'Fill requisites db with fake data.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of fake user requisites')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for _ in range(1, count + 1):
            requisite = Requisite(name=f'Name{_}', surname=f'Surname{_}', patronymic=f'Patronymic{_}',
                                  phone=f'+7-999-{str(_).zfill(7)}', payment_type=choice(['card', 'bill']),
                                  account_type=choice(['debit', 'credit']), limit=randint(10_000, 100_000_000))
            requisite.save()
            print(requisite)
