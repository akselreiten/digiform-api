from django.conf.urls import url

from .views import ApplicationListCreateView, AllApplicationsListCreateView

urlpatterns = [

    url(r'^$',
        ApplicationListCreateView.as_view(),
        name='application-list-create'),

    url(r'^getApplications/$',
        AllApplicationsListCreateView.as_view(),
        name='get-applications'),
]

