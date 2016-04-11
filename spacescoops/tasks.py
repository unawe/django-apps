from django.template import loader, Context, Template
from django.conf import settings
from weasyprint import HTML

from .models import Institution


#TODO: run as daily task?
def populate_article_count():
    for obj in Institution.objects.all():
        obj.spacescoop_count = len(obj.scoops.all())
        obj.save()


def make_pdf(obj):
    template = loader.get_template('spacescoops/article_detail_print.html')
    context = Context({'object': obj, })
    HTML(string=template.render(context), base_url='http://localhost:8004').write_pdf('%s--.pdf' % obj.code)
