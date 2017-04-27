from django.conf.urls import url

from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from .views import UserListCreate, UserHandling

urlpatterns = [

    #authenticate user
    url(r'^api-token-auth/$',
        obtain_jwt_token,
        name='token-auth'),

    #verify user
    url(r'^api-token-verify/$',
        verify_jwt_token,
        name='verify-token'),

    #create user
    url(r'^createUser/$',
        UserListCreate.as_view(),
        name='current-user'),

    #get user
    url(r'^getUser/$',
        UserListCreate.as_view(),
        name='get-user'),

    #logout handling
    url(r'^logout/$',
        UserHandling.as_view(),
        name='logout'),

]

