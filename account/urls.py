from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
urlpatterns = [
    path('api/login/', obtain_auth_token, name='login'),
    path('api/logout_user/', views.logout_user, name="logout_user")
]
