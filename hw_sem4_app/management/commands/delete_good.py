from django.core.management.base import BaseCommand
from hw_sem4_app.models import Good


class Command(BaseCommand):
    help = "Delete good by good_id."
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Good ID')
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        good = Good.objects.filter(pk=pk).first()
        if good is not None:
            good.delete()
        self.stdout.write(f'Good {good.good_name} deleted.')