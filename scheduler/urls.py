from django.urls import path
from . import views

urlpatterns = [
    # Event URLs
    path('events/create/', views.create_event, name='create_event'),
    path('events/update/<int:pk>/', views.update_event, name='update_event'),
    path('events/delete/<int:pk>/', views.delete_event, name='delete_event'),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),

    # Session URLs
    path('sessions/add/', views.add_session, name='add_session'),
    path('sessions/update/<int:pk>/', views.update_session, name='update_session'),
    path('sessions/delete/<int:pk>/', views.delete_session, name='delete_session'),
    path('sessions/', views.session_list, name='session_list'),
    
    
    
    
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
]
