import random
from random import randrange
from datetime import timedelta, datetime
from django.core.management.base import BaseCommand
from django.db.models import Sum, F, DecimalField
from hw_sem4_app.models import Good, Order, Client

the_start = datetime.strptime('2023-01-01', '%Y-%m-%d')
the_end = datetime.strptime('2024-06-12', '%Y-%m-%d')
def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return (start + timedelta(seconds=random_second)).date()
class Command(BaseCommand):
    help = "Create n orders"

    def add_arguments(self, parser):
        parser.add_argument('n', type=int, help='number of orders')

    def get_id_of_all_clients(self):
        clients_ = Client.objects.all()
        client_refs = []
        for one in clients_:
            client_refs.append(one.id)
        return client_refs

    def get_id_of_all_goods(self):
        goods_ = Good.objects.all()
        good_refs = []
        for one in goods_:
            good_refs.append(one.id)
        return good_refs

    def handle(self, *args, **kwargs):
        n = kwargs.get('n')
        for i in range(1, n+1):
            client_id = random.choice(self.get_id_of_all_clients())

            order = Order.objects.create(order_client=Client.objects.filter(pk=client_id).first(),
                                         order_date=random_date(the_start, the_end))
            num = random.randint(1,6)
            good_refs = random.choices(self.get_id_of_all_goods(), k=num)
            for ref in good_refs:
                g = Good.objects.filter(pk=ref).first()
                order.order_items.add(g)
                order.order_total += g.get_good_total()
            if order.order_items:
                order.save()
            self.stdout.write(f'Order added.')





