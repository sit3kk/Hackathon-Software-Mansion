from django.shortcuts import render
from .models import Event, Participant
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.utils.timezone import localtime


class CreateEventView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        user = request.user
        try:
            event = Event.objects.create(
                name=data['name'],
                description=data['description'],
                start_time=data['start_time'],
                end_time=data['end_time'],
                creator=user,
                place=data.get('place', ''),  # Optional fields should use .get()
                photo=data.get('photo', None),  # Assuming you're handling file uploads correctly
                participantsCount=data.get('participantsCount', 0),
                participantsMax=data.get('participantsMax', 0),
                latitude=data['latitude'],
                longitude=data['longitude']
            )
            return Response({'success': 'Event created successfully', 'event_id': event.id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': 'Failed to create event'}, status=status.HTTP_400_BAD_REQUEST)

        

class DeleteEventView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, event_id):
        user = request.user
        event = get_object_or_404(Event, id=event_id, creator=user)
        event.delete()
        return Response({'success': 'Event deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    

class JoinEventView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, event_id):
        user = request.user
        event = get_object_or_404(Event, id=event_id)
        Participant.objects.get_or_create(event=event, user=user)
        return Response({'success': f'Joined the event {event.name} successfully'}, status=status.HTTP_200_OK)




class GetAllEventsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        events = Event.objects.all()
        events_data = [
            {
                'id': event.id,
                'name': event.name,
                'description': event.description,
                'start_time': event.start_time,
                'end_time': event.end_time,
                'creator': event.creator.username,
                'place': event.place,
                # 'photo': event.photo.url if event.photo else None,  # Uncomment if handling photos
                'participantsCount': event.participantsCount,
                'participantsMax': event.participantsMax,
                'latitude': event.latitude,
                'longitude': event.longitude,
            } for event in events
        ]
        return Response(events_data, status=status.HTTP_200_OK)
    
class LeaveEventView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, event_id):
        user = request.user
        event = get_object_or_404(Event, id=event_id)
        participant = get_object_or_404(Participant, event=event, user=user)
        participant.delete()
        return Response({'success': f'Left the event {event.name} successfully'}, status=status.HTTP_204_NO_CONTENT)


class GetEventDetailsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        event_data = {
            'name': event.name,
            'description': event.description,
            'start_time': event.start_time,
            'end_time': event.end_time,
            'creator': event.creator.username,
            'place': event.place,
            # 'photo': event.photo.url if event.photo else None,  # Uncomment if handling photos
            'participantsCount': event.participantsCount,
            'participantsMax': event.participantsMax,
            'latitude': event.latitude,
            'longitude': event.longitude,
            'participants': [{'username': participant.user.username, 'joined_at': participant.joined_at} for participant in event.participants.all()]
        }
        return Response(event_data, status=status.HTTP_200_OK)




class EventParticipantsView(APIView):
    permission_classes = [AllowAny] 

    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        participants = event.participants.all()
        participants_list = [{'username': participant.user.username, 'joined_at': localtime(participant.joined_at).strftime('%Y-%m-%d %H:%M:%S')} for participant in participants]
        return Response({'event': event.name, 'participants': participants_list})
