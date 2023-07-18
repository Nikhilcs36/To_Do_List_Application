from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from . import views
urlpatterns = [
    path('api/login/', obtain_auth_token, name="login"),
    path('api/logout_user/', views.logout_user, name="logout_user"),
    path('api/register/', views.user_register_view, name="register"),
    path('activate/<str:uidb64>/<str:email_token>/', views.activate_account, name="activate"),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framwork')),
    
]
