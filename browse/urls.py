from django.urls import path
from browse import views

app_name = 'browse'

urlpatterns = [
    path('', views.init, name='init'),
    path('posts/', views.posts, name='posts'),
    path('posts/<int:post_id>/', views.post, name='post'),
    path('profiles/<int:user_id>/', views.profile, name='profile'),
]
