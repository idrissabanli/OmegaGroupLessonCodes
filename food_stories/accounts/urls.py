from django.urls import path
from accounts.views import RegisterView, StoriesLoginView, ChangePasswordView, register, login, user_profile, logout


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', StoriesLoginView.as_view(), name='login'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('logout/', logout, name='logout'),
    path('profile/', user_profile, name='user_profile'),
]