from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CategoryListView.as_view(), name='list'),
    url(r'^(?P<slug>.+)?/$', views.CategoryDetailView.as_view(), name='detail'),
]
