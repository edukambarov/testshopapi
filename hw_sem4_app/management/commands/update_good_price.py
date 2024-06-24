import decimal

from django.core.management.base import BaseCommand
from hw_sem4_app.models import Good


class Command(BaseCommand):
    help = "Update good price by id."
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Good ID')
        parser.add_argument('price', type=float, help='Good price')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        price = kwargs.get('price')
        good = Good.objects.filter(pk=pk).first()
        good.price = price
        good.save()
        self.stdout.write(f'Good {good.good_name} price changed.')