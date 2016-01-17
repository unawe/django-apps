

#TODO: run as daily task?
def populate_article_count():
    from .models import OriginalNewsSource
    for obj in OriginalNewsSource.objects.all():
        obj.article_count = len(obj.articles.all())
        obj.save()
