from django.urls import path
from .views import CreateEventView, DeleteEventView, JoinEventView, LeaveEventView, GetAllEventsView, GetEventDetailsView, EventParticipantsView

urlpatterns = [
    path('create/', CreateEventView.as_view(), name='create_event'),
    path('delete/<int:event_id>/', DeleteEventView.as_view(), name='delete_event'),
    path('join/<int:event_id>/', JoinEventView.as_view(), name='join_event'),
    path('leave/<int:event_id>/', LeaveEventView.as_view(), name='leave_event'),
    path('get_events', GetAllEventsView.as_view(), name='get_all_events'),
    path('get_event/<int:event_id>/', GetEventDetailsView.as_view(), name='get_event_details'),
    path('get_event_participants/<int:event_id>/', EventParticipantsView.as_view(), name='get_event_participants'),
]