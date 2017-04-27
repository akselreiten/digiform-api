from django.conf.urls import url

from .views import UniversityReviewListCreateView

urlpatterns = [

    #get and create review
    url(r'^$',
        UniversityReviewListCreateView.as_view(),
        name='university-review-list-create')
]

