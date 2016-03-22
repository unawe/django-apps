from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ActivityListView.as_view(), name='list'),
    url(r'^category/(?P<category>\w+)/$', views.ActivityListView.as_view(), name='list_by_category'),

    url(r'^(?P<code>\d{4})/$', views.detail_by_code),
    url(r'^(?P<code>\d{4})/(?P<slug>.+)?/$', views.ActivityDetailView.as_view(), name='detail'),


]
