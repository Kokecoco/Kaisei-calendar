from django.urls import path
from .views import calendar_view, event_detail

urlpatterns = [
    path('', calendar_view, name='index'),
    path('calendar/', calendar_view, name='calendar'),
    path('event/<int:event_id>/', event_detail, name='event_detail'),
]
