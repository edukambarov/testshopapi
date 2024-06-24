import decimal

from django.core.management.base import BaseCommand
from hw_sem4_app.models import Good


class Command(BaseCommand):
    help = "Update good quantity by id."
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Good ID')
        parser.add_argument('quantity', type=int, help='Good quantity')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        quantity = kwargs.get('quantity')
        good = Good.objects.filter(pk=pk).first()
        good.quantity = quantity
        good.save()
        self.stdout.write(f'Good {good.good_name} quantity changed.')