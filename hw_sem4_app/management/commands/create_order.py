

from django.core.management.base import BaseCommand
from django.db.models import Sum, F, DecimalField
from hw_sem4_app.models import Good, Order, Client


class Command(BaseCommand):
    help = "Create order"

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help='Client ID')
        parser.add_argument('-g', type=int, nargs='*', dest='good_refs',
                      help='List of good IDs',
                    required=True)

    def handle(self, *args, **kwargs):
        client_id = kwargs.get('client_id')
        print(client_id)
        order = Order.objects.create(order_client=Client.objects.filter(pk=client_id).first())
        good_refs = kwargs.get('good_refs')
        print(good_refs)
        for ref in good_refs:
            g = Good.objects.filter(pk=ref).first()
            order.order_items.add(g)
            order.order_total += g.get_good_total()
        if order.order_items:
            order.save()
        self.stdout.write(f'Order added.')








