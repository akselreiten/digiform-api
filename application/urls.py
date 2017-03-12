from django.conf.urls import url

from .views import ApplicationListCreateView, ApplicationListCreate

urlpatterns = [

    url(r'^$',
        ApplicationListCreateView.as_view(),
        name='application-list-create'),

    url(r'^createApplication/$',
        ApplicationListCreate.as_view(),
        name='current-application'),
]
