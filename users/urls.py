from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as users_views 


urlpatterns = [
      path('login/', auth_views.LoginView
         .as_view(template_name='users/login.html'), name='login'),  # class based views (
    # without templates
    # tho)
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password-reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'),
        name='password-reset-done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'),
         name='password-reset-done'),
    path('register/', users_views.register, name='register-users'),
    path('profile/', users_views.profile, name='profile'),
    path('search/', users_views.SearchView, name='search'),
    
]
