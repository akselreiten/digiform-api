from django.conf.urls import url

from .views import UniversityListCreateView, UniversityListSubjectView

urlpatterns = [

    url(r'^$',
        UniversityListCreateView.as_view(),
        name='university-list-create'),

    url(r'^(?P<pk>[0-9]+)/subjects/$',
        UniversityListSubjectView.as_view(),
        name='university-list-subject'
        ),
]