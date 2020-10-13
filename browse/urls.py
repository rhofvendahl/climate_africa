from django.urls import path
from browse import views

app_name = 'browse'

urlpatterns = [
    path('', views.init, name='init'),
    path('posts/', views.posts, name='posts'),
    path('posts/<int:post_id>/', views.post, name='post'),
    # path('posts/<int:post_id>/support/', views.support_post, name='support_post'),
    # path('posts/<int:post_id>/unsupport/', views.unsupport_post, name='unsupport_post'),
    path('profiles/<int:user_id>/', views.profile, name='profile'),
    # path('profiles/<int:user_id>/support/', views.support_user, name='support_user'),
    # path('profiles/<int:user_id>/unsupport', views.unsupport_user, name='unsupport_user'),
]
