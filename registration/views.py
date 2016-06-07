from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from django.core.urlresolvers import reverse_lazy
from registration.forms import *
from django.views.generic import ListView
from django.views.generic import DetailView
from registration.models import Chocolate
from django.http import Http404

# Create your views here.
class CurrentUserMixin(object):
    model = User

    def get_object(self, *args, **kwargs):
        try: obj = super(CurrentUserMixin, self).get_object(*args, **kwargs)
        except AttributeError: obj = self.request.user
        return obj





class Home(ListView):
    template_name="index.html"

    def get_queryset(self):
        return Chocolate.objects.all()




class UserRegistrationView(AnonymousRequiredMixin, FormView):
    template_name = "register_user.html"
    authenticated_redirect_url = reverse_lazy(u"home")
    form_class = UserRegistrationForm
    success_url = '/registration/user/success/'

    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)

class AddchocolateView(FormView):
    template_name = "add_chocolate.html"
    authenticated_redirect_url = reverse_lazy(u"home")
    form_class = chocolateaddForm
    success_url = '/registration/chocolate/success/'

    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)


class ChocolateDetailsView(DetailView):
    template_name = "chocolate_detail.html"

    def get_object(self, queryset=None):
        choco_id = self.kwargs['choco_id']
        obj = Chocolate.objects.get(id=choco_id)
        if obj:
            return obj
        else:
            raise Http404("No details Found.")

class UserProfileUpdateView(LoginRequiredMixin, CurrentUserMixin, UpdateView):
    model = User
    fields = user_fields + user_extra_fields
    template_name= 'user_profile_update.html'
    success_url = '/registration/user/profile/'




