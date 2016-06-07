from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from registration import views
from registration.views import *
from registration.models import *
from django.contrib.auth.decorators import login_required
from registration.views import *
from django.views.generic import UpdateView




urlpatterns = [
    url(r'^$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^user/$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^user/success/', TemplateView.as_view(template_name='success.html'), name='user_registration_success'),
    url(r'^chocolate/add/$', AddchocolateView.as_view(), name='add_chocolate'),
    url(r'^chocolate/info/(?P<choco_id>\d+)/$', ChocolateDetailsView.as_view(), name="chocolate_info"),
    url(r'^user/profile/edit/$', UserProfileUpdateView.as_view(), name='user_profile_update'),
    url(r'^user/profile/edit/success/$', TemplateView.as_view(template_name='user_update_success.html'),
        name='user_profile_update_success'),

]

