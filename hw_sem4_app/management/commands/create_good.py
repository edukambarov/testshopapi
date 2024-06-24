import random
from random import choices


from django.core.management.base import BaseCommand
from hw_sem4_app.models import Good


class Command(BaseCommand):
    help = "Create good"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='number of goods to create')

    def handle(self, *args, **kwargs):

        count = kwargs.get('count')
        for i in range(1, count + 1):
            good = Good(good_name=f'Good_{i}',
                        description=f"This is good {i}",
                        price=round(random.randint(100,100000)/100,2),
                        quantity=random.randint(1,21),)
            good.save()
            self.stdout.write(f'Good {good.good_name} added.')