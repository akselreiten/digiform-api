from django.conf.urls import url

from .views import SubjectListCreateView,SubjectCreateView

urlpatterns = [


    #creating view of all subjects
    url(r'^$',
        SubjectListCreateView.as_view(),
        name='subject-list-create'),


    #a pk from 0 to 9 is sent with the url,
    #defining the subject id.

    url(r'^(?P<pk>[0-9]+)/$',
        SubjectCreateView.as_view(),
        name='get-subject'
        ),

]