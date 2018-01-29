from django.conf.urls import url
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token)

from . import views


urlpatterns = [
    # obtain_jwt_token sends us a token if user is properly logged
    url(r'^jwt/create/', obtain_jwt_token),
    url(r'^jwt/refresh/', refresh_jwt_token),
    url(r'^jwt/verify', verify_jwt_token),
    url(r'^users/(?P<pk>\d+)/$', views.UsersDetailView.as_view()),
    url(r'^register/$', views.UserRegister.as_view()),
    url(r'^users/$', views.UsersListView.as_view()),
]