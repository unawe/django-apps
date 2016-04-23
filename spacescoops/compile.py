import os
import logging

# from django.template import loader, Context, Template
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import activate
from weasyprint import HTML
from contrib.urlfetch import url_read

from .models import Article


logger = logging.getLogger(__name__)
OUT_PATH = os.path.join(settings.MEDIA_ROOT, 'articles', 'download')
OUT_URL = os.path.join(settings.MEDIA_URL, 'articles', 'download')
LANGUAGES = [code for (code, name) in settings.LANGUAGES]


def make_pdf(code, lang, site_url=None):
    if not site_url:
        site_url = settings.SITE_URL
    if code == 'all':
        if lang == 'all':
            for baseobj in Article.objects.available():
                for lang in baseobj.get_available_languages():
                    if lang in LANGUAGES:
                        obj = Article.objects.available().language(lang).get(code=baseobj.code)
                        generate_pdf(obj, site_url)
        else:
            for obj in Article.objects.available().language(lang):
                generate_pdf(obj, site_url)
    else:
        if lang == 'all':
            baseobj = Article.objects.available().get(code=code)
            for lang in baseobj.get_available_languages():
                if lang in LANGUAGES:
                    obj = Article.objects.available().language(lang).get(code=code)
                    generate_pdf(obj, site_url)
        else:
            obj = Article.objects.available().language(lang).get(code=code)
            generate_pdf(obj, site_url)


def _get_filename(code, language_code, slug):
    return 'spacescoop-%s%s-%s.pdf' % (code, language_code, slug)


def get_pdf(code, lang):
    obj = Article.objects.available().language(lang).get(code=code)
    filename = _get_filename(obj.code, obj.language_code, obj.slug)
    if not os.path.exists(os.path.join(OUT_PATH, filename)):
        generate_pdf(obj, settings.SITE_URL)
    return os.path.join(OUT_URL, filename)


def generate_pdf(obj, site_url):
    print(obj.code, obj.language_code)
    activate(obj.language_code)
    url = site_url + reverse('scoops:print-preview', kwargs={'code': obj.code, })
    print(obj.code, obj.language_code, url)
    filename = _get_filename(obj.code, obj.language_code, obj.slug)
    # template = loader.get_template('spacescoops/article_detail_print.html')
    # context = Context({'object': obj, })
    # text = template.render(context)
    text = url_read(url)
    HTML(string=text, base_url=site_url).write_pdf(os.path.join(OUT_PATH, filename))
