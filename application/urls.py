from django.conf.urls import url

from .views import ApplicationListCreateView, AllApplicationsListCreateView

urlpatterns = [

    url(r'^$',
        ApplicationListCreateView.as_view(),
        name='application-list-create'),

    url(r'^getAllApplications/$',
        AllApplicationsListCreateView.as_view(),
        name='get-all-applications'),
]

