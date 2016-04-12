import os
import logging

# from django.template import loader, Context, Template
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import activate
from weasyprint import HTML
from contrib.urlfetch import url_read

from .models import Activity


logger = logging.getLogger(__name__)
OUT_PATH = os.path.join(settings.MEDIA_ROOT, 'activities', 'download')
LANGUAGES = [code for (code, name) in settings.LANGUAGES]


def make_pdf(code, lang, site_url=None):
    if not site_url:
        site_url = settings.SITE_URL
    if code == 'all':
        if lang == 'all':
            for baseobj in Activity.objects.available():
                for lang in baseobj.get_available_languages():
                    if lang in LANGUAGES:
                        obj = Activity.objects.available().language(lang).get(code=baseobj.code)
                        generate_pdf(obj, site_url)
        else:
            for obj in Activity.objects.available().language(lang):
                generate_pdf(obj, site_url)
    else:
        if lang == 'all':
            baseobj = Activity.objects.available().get(code=code)
            for lang in baseobj.get_available_languages():
                if lang in LANGUAGES:
                    obj = Activity.objects.available().language(lang).get(code=code)
                    generate_pdf(obj, site_url)
        else:
            obj = Activity.objects.available().language(lang).get(code=code)
            generate_pdf(obj, site_url)


def generate_pdf(obj, site_url):
    print(obj.code, obj.language_code)
    activate(obj.language_code)
    url = site_url + reverse('activities:print-preview', kwargs={'code': obj.code, })
    print(obj.code, obj.language_code, url)
    filename = 'activity-%s%s-%s.pdf' % (obj.code, obj.language_code, obj.slug)
    # template = loader.get_template('activities/activity_detail_print.html')
    # context = Context({'object': obj, })
    # text = template.render(context)
    text = url_read(url)
    HTML(string=text, base_url=site_url).write_pdf(os.path.join(OUT_PATH, filename))
