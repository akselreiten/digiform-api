from django.conf.urls import url

from .views import ApplicationListCreateView

urlpatterns = [

    url(r'^$',
        ApplicationListCreateView.as_view(),
        name='application-list-create')
]

