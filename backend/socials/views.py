# views.py

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Follow
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from events.models import Event

class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, username):
        user_to_follow = get_object_or_404(User, username=username)
        if request.user != user_to_follow:
            Follow.objects.get_or_create(follower=request.user, followed=user_to_follow)
            return Response({'status': 'following'}, status=status.HTTP_200_OK)
        return Response({'error': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)

class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, username):
        user_to_unfollow = get_object_or_404(User, username=username)
        follow_relationship = Follow.objects.filter(follower=request.user, followed=user_to_unfollow)
        if follow_relationship.exists():
            follow_relationship.delete()
            return Response({'status': 'unfollowed'}, status=status.HTTP_200_OK)
        return Response({'error': 'Follow relationship does not exist'}, status=status.HTTP_400_BAD_REQUEST)


class GetFollowingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        following_users = Follow.objects.filter(follower=request.user)
        following_usernames = [follow.followed.username for follow in following_users]
        return Response({'following_users': following_usernames}, status=status.HTTP_200_OK)


class GetFollowersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        followers = Follow.objects.filter(followed=request.user)
        follower_usernames = [follow.follower.username for follow in followers]
        return Response({'followers': follower_usernames}, status=status.HTTP_200_OK)


class GetFollowingEventsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        following_users = Follow.objects.filter(follower=request.user)
        following_usernames = [follow.followed.username for follow in following_users]

        following_events = Event.objects.filter(creator__username__in=following_usernames)


        return Response({'following_events': following_events}, status=status.HTTP_200_OK)
