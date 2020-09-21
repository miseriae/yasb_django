from django.urls import path
from django.contrib.auth import views as auth_views

from .views import UserRegisterView, UserUpdateView, ChangePasswordView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit-profile/', UserUpdateView.as_view(), name='edit-profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'))
    path('password/', ChangePasswordView.as_view(template_name='registration/change-password.html'))
]
