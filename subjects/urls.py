from django.conf.urls import url

from .views import SubjectListCreateView
from .views import NtnuSubjectListCreateView

urlpatterns = [

    url(r'^$',
        NtnuSubjectListCreateView.as_view(),
        name='subject-list-create')
]