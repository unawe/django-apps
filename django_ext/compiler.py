import os
import time

# from django.template import loader, Context, Template
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import activate
from weasyprint import HTML
from contrib.urlfetch import url_read


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
        # print(obj.code, obj.language_code)
        activate(obj.language_code)
        url = site_url + reverse(self.print_preview_urlpath, kwargs={'code': obj.code, })
        # print(obj.code, obj.language_code, url)
        filename = self.pdf_filename(obj)
        text = url_read(url)
        HTML(string=text, base_url=site_url).write_pdf(os.path.join(self.out_path, filename))
