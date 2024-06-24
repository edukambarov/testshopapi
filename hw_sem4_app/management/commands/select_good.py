from django.core.management.base import BaseCommand
from hw_sem4_app.models import Good


class Command(BaseCommand):
    help = "Get Goods with <arg> in name."
    def add_arguments(self, parser):
        parser.add_argument('arg', type=str, help='Argument to be searched within good_name')
    def handle(self, *args, **kwargs):
        arg = kwargs['arg']
        goods = Good.objects.filter(good_name__icontains=arg)
        self.stdout.write(f'{goods}')
