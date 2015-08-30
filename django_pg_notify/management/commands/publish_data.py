"""
Performs Postgres LISTEN and publish data as websocket
"""

from django.core.management.commands.base import BaseCommand
from django.db.models import cursors

class Command(BaseCommand):


    def handle(self, *args, **options):
        pass
