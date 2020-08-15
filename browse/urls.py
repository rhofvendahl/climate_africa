from django.urls import path
from browse import views

app_name = 'browse'

urlpatterns = [
    path('', views.init, name='init'),
    path('posts/', views.posts, name='posts'),
]
