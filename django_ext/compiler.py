import os
import time
import importlib

# from django.template import loader, Context, Template
from django.conf import settings
from django.utils.translation import activate

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger('kokotko')


def get_python_thing(fullname):
    module_name, thing_name = fullname.rsplit('.', 1)
    module = importlib.import_module(module_name)
    return getattr(module, thing_name)


def get_generated_url(objdef, file_type, code, lang=None):
    model = get_python_thing(objdef['model'])
    if lang:
        obj = model.objects.available().language(lang).get(code=code)
        activate(lang)  # required if called from command line ??? TODO: check
        filename = objdef['filename_tpl'] % {'slug': obj.slug, 'code': obj.code, 'lang': obj.language_code, 'ext': file_type}
    else:
        obj = model.objects.available().get(code=code)
        filename = objdef['filename_tpl'] % {'slug': obj.slug, 'code': obj.code, 'ext': file_type}
    path = os.path.join(settings.MEDIA_ROOT, objdef['path'], filename)
    if not (os.path.exists(path) and os.path.getmtime(path) > time.mktime(obj.modification_date.timetuple())):
        renderer = get_python_thing(objdef['renderers'][file_type])
        renderer(obj, path, site_url=settings.SITE_URL)
    return settings.MEDIA_URL + objdef['path'] + filename


# LANGUAGES = [code for (code, name) in settings.LANGUAGES]

# class PdfCompiler(object):

#     def __init__(self, clazz, out_path, out_url, pdf_filename, print_preview_urlpath):
#         self.clazz = clazz
#         self.out_path = out_path
#         self.out_url = out_url
#         self.pdf_filename = pdf_filename
#         self.print_preview_urlpath = print_preview_urlpath

#     def make_pdf(self, code, lang, site_url):
#         if code == 'all':
#             if lang == 'all':
#                 for baseobj in self.clazz.objects.available():
#                     for lang in baseobj.get_available_languages():
#                         if lang in LANGUAGES:
#                             obj = self.clazz.objects.available().language(lang).get(code=baseobj.code)
#                             self.generate_pdf(obj, site_url)
#             else:
#                 for obj in self.clazz.objects.available().language(lang):
#                     self.generate_pdf(obj, site_url)
#         else:
#             if lang == 'all':
#                 baseobj = self.clazz.objects.available().get(code=code)
#                 for lang in baseobj.get_available_languages():
#                     if lang in LANGUAGES:
#                         obj = self.clazz.objects.available().language(lang).get(code=code)
#                         self.generate_pdf(obj, site_url)
#             else:
#                 obj = self.clazz.objects.available().language(lang).get(code=code)
#                 self.generate_pdf(obj, site_url)

#     def get_pdf(self, code, lang, pdf_type):
#         """
#         :param code: id of text to generate
#         :param lang: language of PDF
#         :param pdf_type: type of pdf to generate. every type can has own templates.
#         :return: path to PDF
#         """

#         obj = self.clazz.objects.available().language(lang).get(code=code)
#         filename = self.pdf_filename(obj)
#         path = os.path.join(self.out_path, filename)
#         if not (os.path.exists(path) and os.path.getmtime(path) > time.mktime(obj.modification_date.timetuple())):
#             if pdf_type == 'activities':
#                 self.generate_activities_pdf(obj, settings.SITE_URL)
#             elif pdf_type == 'scoops':
#                 self.generate_scoops_pdf(obj, settings.SITE_URL)
#             else:
#                 raise Exception('type of PDF document is not set')
#         return os.path.join(self.out_url, filename)
