from django.conf.urls import url

from .views import SubjectListCreateView,SubjectCreateView

urlpatterns = [

    url(r'^$',
        SubjectListCreateView.as_view(),
        name='subject-list-create'),

    url(r'^(?P<pk>[0-9]+)/$',
        SubjectCreateView.as_view(),
        name='subject-create'
        ),

]