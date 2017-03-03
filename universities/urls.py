from django.conf.urls import url

from .views import UniversityListCreateView

urlpatterns = [

    url(r'^$',
        UniversityListCreateView.as_view(),
        name='university-list-create')
]