from django.urls import path
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('follow/<str:username>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<str:username>/', UnfollowUserView.as_view(), name='unfollow_user'),
]