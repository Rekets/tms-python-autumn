from django.contrib.auth.models import User
from django.views.generic import TemplateView, DeleteView, \
    UpdateView

from home.models import Articles


class UserDetailView(TemplateView):
    model = User
    template_name = 'user/profile.html'
    slug_field = 'username'
    pk_url_kwarg = 'username'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        # print(context)
        context['articles'] = Articles.objects.all
        return context


class UserUpdateView(UpdateView):
    model = User
    template_name = 'user/edit_profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'user'
    fields = ['username', 'first_name', 'last_name']
    success_url = '/article/'


class UserDeleteView(DeleteView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'user/delete_profile.html'
    success_url = '/articles/'
