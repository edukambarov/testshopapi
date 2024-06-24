import datetime

from django.core.management.base import BaseCommand
from hw_sem4_app.models import Client


class Command(BaseCommand):
    help = "Create client"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='number of Clients to create')
    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(client_name=f'Client_{i}',
                            email=f'mail{i}@pochta.ru',
                            phone=f'{89000000000 + i}',
                            address=f'Street {i}, House {i}, Apartment {i^2}',
                            )
            client.save()
            self.stdout.write(f'Client {client.client_name} added.')