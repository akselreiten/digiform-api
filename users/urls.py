from django.conf.urls import url

from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from .views import UserListCreate

urlpatterns = [
    url(r'^api-token-auth/$',
        obtain_jwt_token,
        name='token-auth'),

    url(r'^api-token-verify/$',
        verify_jwt_token,
        name='verify-token'),

    url(r'^createUser/$',
        UserListCreate.as_view(),
        name='current-user'),

]

