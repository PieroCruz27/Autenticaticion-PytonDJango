from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views
app_name = 'account'

urlpatterns = [
   # path('login/', views.user_login, name='login'),  # Ruta para la vista de login
  path('login/', auth_views.LoginView.as_view(), name='login'), #login
  path('logout/', auth_views.LogoutView.as_view(), name='logout'), #logout
   # path('password-change/', para cambiar contraseña
  path('password-change/',auth_views.PasswordChangeView.as_view(), name='password_change'), #cambiar contrasena
  path('password-change/done/',auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'), #fin de cambio de contrasena
  # para resetar pasword
  path('password-reset/',auth_views.PasswordResetView.as_view(), name='password_reset'), #resetar
  path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'), #resetar fin
  path('password-reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'), #resetar confirmar
  path('password-reset/complete/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),#resetar completo
  # registrar
  path('register/', views.register, name='register'),

  path('edit/', views.edit, name='edit'),

  path('dashboard/', views.dashboard, name='dashboard'),
]

