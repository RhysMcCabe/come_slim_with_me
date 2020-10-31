from django.urls import path
from .views import SignUpView, ForgotPasswordView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/login/password_reset', ForgotPasswordView.as_view(), name='password_reset')
]