from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView

from .forms import SignUpForm, EditProfileForm, ChangePasswordForm


class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('home')


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserUpdateView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit-profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
