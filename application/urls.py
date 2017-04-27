from django.conf.urls import url

from .views import ApplicationListCreateView, AllApplicationsListCreateView

urlpatterns = [


    #creating application view of own applications
    url(r'^$',
        ApplicationListCreateView.as_view(),
        name='application-list-create'),

    #creating application view of all applications
    url(r'^getApplications/$',
        AllApplicationsListCreateView.as_view(),
        name='get-applications'),
]

