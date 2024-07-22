
from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='home'),
	path('upload/', views.upload, name='upload'),
	path('video/<int:id>', views.video, name='video'),
	path('register/', views.register, name='register'),
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),
	path('author/<int:id>', views.author, name='author')
]

