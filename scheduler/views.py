from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Event, Session
from .forms import EventForm, SessionForm

# Event Views
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Redirect to a list view or another relevant page
    else:
        form = EventForm()
    return render(request, 'event.html', {'form': form})

def update_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'update_event.html', {'form': form})


def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event_detail.html', {'event': event})

# Session Views
def add_session(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('session_list')
    else:
        form = SessionForm()
    return render(request, 'add_session.html', {'form': form})

def update_session(request, pk):
    session = get_object_or_404(Session, pk=pk)
    if request.method == 'POST':
        form = SessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('session_list')
    else:
        form = SessionForm(instance=session)
    return render(request, 'update_session.html', {'form': form})

def delete_session(request, pk):
    session = get_object_or_404(Session, pk=pk)
    if request.method == 'POST':
        session.delete()
        return redirect('session_list')
    return render(request, 'delete_session.html', {'session': session})

def session_list(request):
    sessions = Session.objects.all()
    return render(request, 'session_list.html', {'sessions': sessions})





def home(request):
    return render(request, 'home.html')

def events(request):
    return render(request, 'events.html')

