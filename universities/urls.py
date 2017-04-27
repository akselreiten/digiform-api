from django.conf.urls import url

from .views import UniversityListCreateView, UniversityListSubjectView, UniversitySearchListCreateView

urlpatterns = [

    #get all universities;create university
    url(r'^$',
        UniversityListCreateView.as_view(),
        name='university-list-create'),


    #get specific university by id (pk)
    url(r'^(?P<pk>[0-9]+)/subjects/$',
        UniversityListSubjectView.as_view(),
        name='university-list-subject'
        ),

    #get universities based on filters
    url(r'^getUniversities/$',
        UniversitySearchListCreateView.as_view(),
        name='university-list-create'),
]