from django.conf.urls import patterns, url, include
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from notesapi.v1.views import AnnotationListView, AnnotationDetailView, AnnotationSearchView

urlpatterns = patterns('',  # nopep8
    url(r'^annotations/$', AnnotationListView.as_view(), name='annotations'),
    url(r'^annotations/(?P<annotation_id>[a-zA-Z0-9_-]+)$', AnnotationDetailView.as_view(), name='annotations_detail'),
    url(r'^search$', AnnotationSearchView.as_view(), name='annotations_search'),
    url(r'^status/$', RedirectView.as_view(url=reverse_lazy('status')), name='status'),
)
