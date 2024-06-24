from django.core.management.base import BaseCommand
from hw_sem4_app.models import Client


class Command(BaseCommand):
    help = "Get Clients with <arg> in name."
    def add_arguments(self, parser):
        parser.add_argument('arg', type=str, help='Argument to be searched within name')
    def handle(self, *args, **kwargs):
        arg = kwargs['arg']
        clients = Client.objects.filter(client_name__icontains=arg)
        self.stdout.write(f'{clients}')
