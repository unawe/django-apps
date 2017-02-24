import os
import time

# from django.template import loader, Context, Template
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import activate
from weasyprint import HTML
from contrib.urlfetch import url_read
from urllib.parse import urljoin

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger('kokotko')

LANGUAGES = [code for (code, name) in settings.LANGUAGES]


class PdfCompiler(object):

    def __init__(self, clazz, out_path, out_url, pdf_filename, print_preview_urlpath):
        self.clazz = clazz
        self.out_path = out_path
        self.out_url = out_url
        self.pdf_filename = pdf_filename
        self.print_preview_urlpath = print_preview_urlpath

    def make_pdf(self, code, lang, site_url):
        if code == 'all':
            if lang == 'all':
                for baseobj in self.clazz.objects.available():
                    for lang in baseobj.get_available_languages():
                        if lang in LANGUAGES:
                            obj = self.clazz.objects.available().language(lang).get(code=baseobj.code)
                            self.generate_pdf(obj, site_url)
            else:
                for obj in self.clazz.objects.available().language(lang):
                    self.generate_pdf(obj, site_url)
        else:
            if lang == 'all':
                baseobj = self.clazz.objects.available().get(code=code)
                for lang in baseobj.get_available_languages():
                    if lang in LANGUAGES:
                        obj = self.clazz.objects.available().language(lang).get(code=code)
                        self.generate_pdf(obj, site_url)
            else:
                obj = self.clazz.objects.available().language(lang).get(code=code)
                self.generate_pdf(obj, site_url)

    def get_pdf(self, code, lang):
        obj = self.clazz.objects.available().language(lang).get(code=code)
        filename = self.pdf_filename(obj)
        path = os.path.join(self.out_path, filename)
        if not (os.path.exists(path) and os.path.getmtime(path) > time.mktime(obj.modification_date.timetuple())):
            self.generate_pdf(obj, settings.SITE_URL)
        return os.path.join(self.out_url, filename)

    # def pdf_filename(self, code, language_code, slug):
    #     return 'activity-%s%s-%s.pdf' % (code, language_code, slug)

    def generate_pdf(self, obj, site_url):
        activate(obj.language_code)

        # first page
        header_url = urljoin(site_url,reverse('activities:print-preview-header', kwargs={'code': obj.code, }))
        header_html_source = url_read(header_url)
        header = HTML(string=header_html_source, base_url=site_url).render()

        # other pages
        content_url = urljoin(site_url, reverse('activities:print-preview-content', kwargs={'code': obj.code, }))
        content_html_source = url_read(content_url)
        content = HTML(string=content_html_source, base_url=site_url).render()

        header.pages += content.pages
        filename = self.pdf_filename(obj)

        header.write_pdf(os.path.join(self.out_path, filename))



