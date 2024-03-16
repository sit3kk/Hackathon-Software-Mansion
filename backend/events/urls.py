from django.urls import path
from .views import CreateEventView, DeleteEventView, JoinEventView, LeaveEventView, GetAllEventsView, GetEventDetailsView

urlpatterns = [
    path('events/create/', CreateEventView.as_view(), name='create_event'),
    path('events/delete/<int:event_id>/', DeleteEventView.as_view(), name='delete_event'),
    path('events/join/<int:event_id>/', JoinEventView.as_view(), name='join_event'),
    path('events/leave/<int:event_id>/', LeaveEventView.as_view(), name='leave_event'),
    path('events/', GetAllEventsView.as_view(), name='get_all_events'),
    path('events/<int:event_id>/', GetEventDetailsView.as_view(), name='get_event_details'),
]