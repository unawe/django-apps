from django.http import HttpResponse, Http404, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.core.urlresolvers import reverse

from django.views.generic import ListView, DetailView
from parler.views import TranslatableSlugMixin, ViewUrlMixin, FallbackLanguageResolved
from django.contrib.syndication.views import Feed

from spaceawe import misc
from activities.models import Activity, Collection, ACTIVITY_SECTIONS, ACTIVITY_METADATA


# def list(request):
#     lst = get_list_or_404(Activity, user=request.user, order_by='-release_date')
#     return render(request, 'activities/list.html', {'object_list': lst, })


def _activity_queryset(request, only_translations=True):
    qs = Activity.objects.available(user=request.user)
    if only_translations:
        qs = qs.active_translations()
    qs = Activity.add_prefetch_related(qs)
    return qs


class ActivityListView(ViewUrlMixin, ListView):
    # template_name = 'activities/list.html'
    page_template_name = 'activities/activity_list_page.html'
    # context_object_name = 'object_list'
    # model = Activity
    view_url_name = 'activities:list'
    # paginate_by = 10

    def get_queryset(self):
        qs = _activity_queryset(self.request)
        if 'category' in self.kwargs:
            category = self.kwargs['category']
            qs = qs.filter(**{category: True})
        return qs

    def get_view_url(self):
        if 'category' in self.kwargs:
            return reverse('activities:list_by_category', kwargs={'category': self.kwargs['category']})
        else:
            return super().get_view_url()

    def get_template_names(self):
        if self.request.is_ajax():
            return [self.page_template_name]
        else:
            return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_template'] = self.page_template_name
        return context


#
# def detail(request, code, slug):
#     obj = get_object_or_404(Activity, user=request.user, code=code)
#     return render(request, 'activities/detail.html', {
#             'object': obj,
#             'sections': ACTIVITY_SECTIONS,
#             'sections_meta': ACTIVITY_METADATA,
#             'random': Activity.objects.available().order_by('?')[:3]
#         })

# def detail_by_code(request, code):
#     obj = get_object_or_404(Activity, user=request.user, code=code)
#     return HttpResponsePermanentRedirect(obj.get_absolute_url())


class ActivityDetailView(DetailView):
    # model = Activity
    # template_name = 'activities/detail.html'
    slug_field = 'code'
    slug_url_kwarg = 'code'

    def get_queryset(self, only_translations=False):
        qs = _activity_queryset(self.request, only_translations=only_translations)
        # qs = qs.prefetch_related('originalnews_set')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sections'] = ACTIVITY_SECTIONS
        context['sections_meta'] = ACTIVITY_METADATA
        # context['random'] = self.get_queryset(only_translations=True).order_by('?')[:3]
        context['random'] = misc.spaceawe_random_resources(self.object)
        return context


class ActivityDetailPrintView(ActivityDetailView):
    template_name = 'activities/activity_detail_print.html'


def detail_by_code(request, code):
    'When only the code is provided, redirect to the canonical URL'
    obj = _activity_queryset(request).get(code=code)
    return redirect(obj, permanent=True)


class ActivityFeed(Feed):
    title = 'Activities'
    link = '/'
    # link = reverse('scoops:list')
    # description = ''

    def items(self):
        return Activity.objects.available().translated()[:9]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('activities:detail', kwargs={'code': item.code, 'slug': item.slug})

# def collections_list(request):
#     lst = get_list_or_404(Collection, user=request.user)
#     return render(request, 'collections/list.html', {'object_list': lst, })

# def collections_detail(request, collection_slug):
#     obj = get_object_or_404(Collection, user=request.user, slug=collection_slug)
#     return render(request, 'collections/detail.html', {'object': obj})

class CollectionListView(ViewUrlMixin, ListView):
    # template_name = 'collections/list.html'
    # context_object_name = 'object_list'
    model = Collection
    view_url_name = 'collections:list'
    # paginate_by = 10


class CollectionDetailView(DetailView):
    # model = Collection
    # template_name = 'collections/detail.html'
    # slug_field = 'slug'
    slug_url_kwarg = 'collection_slug'
