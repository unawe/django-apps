from django.core.management.base import BaseCommand

from spacescoops.tasks import make_pdf
from spacescoops.models import Article


class Command(BaseCommand):
    help = 'Populates aggregate fields'

    def handle(self, *args, **options):
        code = '1601'
        lang = 'en'
        assert(lang is not None)
        obj = Article.objects.language(lang).get(code=code)
        make_pdf(obj)
