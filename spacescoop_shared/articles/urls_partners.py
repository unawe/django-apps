from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PartnerListView.as_view(), name='list'),
    url(r'^(?P<slug>.+)?/$', views.PartnerDetailView.as_view(), name='detail'),
]
