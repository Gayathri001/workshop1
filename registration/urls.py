from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from registration import views
from registration.views import *
from registration.models import *
from django.contrib.auth.decorators import login_required
from registration.views import *




urlpatterns = [
    url(r'^$', UserRegistrationView.as_view(), name='register_user')]