'''urls for authentication'''
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, \
    password_reset_complete
from django.urls import path

from auth.views import UserSignUpView, ActivateUserView, UserSigninView,  UserRenameView

app_name = 'auth'
urlpatterns = [
    path('login/', UserSigninView.as_view(), name='login'),
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('<int:pk>/rename/', login_required(UserRenameView.as_view()), name='rename'),
    path('activate/<str:uidb64>/<str:token>', ActivateUserView.as_view(), name='activate'),
    path('reset-password/', password_reset,
         {'template_name': 'auth/reset_password.html',
          'post_reset_redirect': 'auth:password_reset_done',
          'email_template_name': 'auth/reset_password_email.html'},
         name='reset_password'),

    path(r'reset-password/done/', password_reset_done, {'template_name': 'auth/reset_password_done.html'},
         name='password_reset_done'),

    path(r'reset-password/confirm/<str:uidb64>/<str:token>/', password_reset_confirm,
         {'template_name': 'auth/reset_password_confirm.html',
          'post_reset_redirect': 'auth:password_reset_complete'}, name='password_reset_confirm'),

    path('reset-password/complete/', password_reset_complete,
         {'template_name': 'auth/reset_password_complete.html'}, name='password_reset_complete')

]
