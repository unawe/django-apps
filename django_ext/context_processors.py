from django.conf import settings


def thumbnail_aliases(request):
    return {'THUMBNAIL_ALIASES': settings.THUMBNAIL_ALIASES}
