from django.conf.urls import url
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.ActivityListView.as_view(), name='list'),
    url(r'^feed/$', views.ActivityFeed(), name='feed'),
    url(r'^(?P<code>\d{4})/$', views.detail_by_code),
    url(r'^(?P<code>\d{4})/print-preview/$', views.ActivityDetailPrintView.as_view(), name='print-preview'),
    # url(r'^(?P<code>\d{4})/print/$', views.activity_pdf, name='print'),
    url(r'^(?P<code>\d{4})/(?P<slug>.+)?/$', views.ActivityDetailView.as_view(), name='detail'),
]

if settings.SHORT_NAME == 'spaceawe':
    urlpatterns += [
        url(r'^category/(?P<category>\w+)/$', views.ActivityListView.as_view(), name='list_by_category'),
    ]
