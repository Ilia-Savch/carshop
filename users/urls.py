from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView

from . import views
from django.urls import path, reverse_lazy

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('register/', views.RegisterUser.as_view(), name='register'),

    path('profile/<int:pk>', views.DetailProfile.as_view(), name='profile'),
    path('change_profile/<int:pk>', views.ChangeProfile.as_view(), name='change_profile'),

    path('change_password/', views.UserPasswordChange.as_view(), name='password_change'),
    path('change_password_done/', PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"),
         name='password_change_done'),

    path('password_reset/', PasswordResetView.as_view(template_name='users/password_reset_form.html',
                                                      success_url=reverse_lazy('password_reset_done')),
         name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),

    path('password_reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',
                                          success_url=reverse_lazy('password_reset_complete')),
         name='password_reset_confirm'),
    path('password_reset/complete',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete')

]
