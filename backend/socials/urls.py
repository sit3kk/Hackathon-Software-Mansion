from django.urls import path
from .views import FollowUserView, UnfollowUserView, GetFollowingView, GetFollowersView, GetFollowingEventsView

urlpatterns = [
    path('follow/<str:username>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<str:username>/', UnfollowUserView.as_view(), name='unfollow_user'),
    path('get_following/', GetFollowingView.as_view(), name='get_following'),
    path('get_followers/', GetFollowersView.as_view(), name='get_followers'),
    path('get_following_events/', GetFollowingEventsView.as_view(), name='get_following_events'),
    
]