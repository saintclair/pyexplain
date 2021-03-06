import views
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(
        r'^create/(?P<app_label>\w+)/(?P<model>\w+)/(?P<obj_id>\d+)/$',
        views.LinkCreateView.as_view(),
        name='create'
    ),
    url(
        r'^update/(?P<pk>\d+)/$',
        views.LinkUpdateView.as_view(),
        name='update'
    ),
)
