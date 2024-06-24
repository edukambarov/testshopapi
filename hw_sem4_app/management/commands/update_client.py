from django.core.management.base import BaseCommand
from hw_sem4_app.models import Client


class Command(BaseCommand):
    help = "Update Client name by id."
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='Client name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        client = Client.objects.filter(pk=pk).first()
        client.client_name = name
        client.save()
        self.stdout.write(f'Client {client.client_name} changed.')