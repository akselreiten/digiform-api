from django.conf.urls import url

from .views import SubjectListCreateView

urlpatterns = [

    url(r'^$',
        SubjectListCreateView.as_view(),
        name='subject-list-create'),

]