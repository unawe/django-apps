from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^(?P<object_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.ArticleListView.as_view(), name='list'),
    # url(r'^category/(?P<slug>[\w-]+)/$', news_views.category, name='category'),
    # url(r'^tag/(?P<slug>[\w-]+)/$', news_views.tag, name='tag'),
    # url(r'^year/(?P<year>\d+)/$', news_views.year, name='year'),
    # url(r'^date/(?P<year>\d+)/$', news_views.date, name='date'),
    
    url(r'^(?P<code>\d{4})/(?P<slug>.+)?/$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^(?P<code>\d{4})/$', views.detail_by_code),

    # url(r'^(?P<code>\d{4})/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail_pk'),
]