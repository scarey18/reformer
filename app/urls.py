from django.urls import path

from . import views


urlpatterns = [
	path('users/register', views.UserCreate.as_view(), name='register'),
	path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
]