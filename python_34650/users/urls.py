

from django.urls import path
#from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from users.views import login_view

urlpatterns = [
    path('login/', login_view),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
]