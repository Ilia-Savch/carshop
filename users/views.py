from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import LoginUsersForm, RegisterUsersForm, ProfileUsersForm, UserPasswordChangeForm


class LoginUser(LoginView):
    form_class = LoginUsersForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = RegisterUsersForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


class DetailProfile(DetailView):
    model = get_user_model()
    template_name = 'users/profile.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ChangeProfile(UpdateView):
    model = get_user_model()
    form_class = ProfileUsersForm
    template_name = 'users/change_profile.html'
    success_url = 'home'

    def get_success_url(self):
        return reverse_lazy('profile', args=[self.request.user.pk])

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'users/password_change_form.html'
