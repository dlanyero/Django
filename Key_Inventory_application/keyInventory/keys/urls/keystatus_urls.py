from django.conf.urls import url
from ..views import (keystatusListView, keystatusCreateView, keystatusDetailView,
                     keystatusUpdateView, keystatusDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        keystatusCreateView.as_view(),
        name="keystatus_create"),

    url(r'^(?P<pk>\d+)/update/$',
        keystatusUpdateView.as_view(),
        name="keystatus_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        keystatusDeleteView.as_view(),
        name="keystatus_delete"),

    url(r'^(?P<pk>\d+)/$',
        keystatusDetailView.as_view(),
        name="keystatus_detail"),

    url(r'^$',
        keystatusListView.as_view(),
        name="keystatus_list"),
]