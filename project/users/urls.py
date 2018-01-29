from django.conf.urls import url

from . import views

urlpatterns = [
    # registration
    url(r'^register/$', views.sign_up, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
]