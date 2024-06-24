from django.core.management.base import BaseCommand
from hw_sem4_app.models import Order


class Command(BaseCommand):
    help = "Get Orders by Client."
    def add_arguments(self, parser):
        parser.add_argument('id_', type=int, help='Client ID')
    def handle(self, *args, **kwargs):
        id_ = kwargs['id_']
        orders = Order.objects.filter(order_client=id_)
        self.stdout.write(f'{orders}')
