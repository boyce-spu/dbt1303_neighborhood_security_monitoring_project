from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, SignInForm, IncidentForm
from .models import Incident, Comment

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect to home page
        else:
            form_errors = form.errors.as_data()
            if '__all__' in form_errors:
                messages.error(request, form_errors['__all__'][0].message)
            else:
                messages.error(request, form_errors)

    else:
        form = SignUpForm()
    return render(request, 'sign-up.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Redirect to home page
        else:
            form_errors = form.errors.as_data()
            if '__all__' in form_errors:
                messages.error(request, form_errors['__all__'][0].message)
            else:
                messages.error(request, form_errors)

    else:
        form = SignInForm()
    return render(request, 'sign-in.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('sign-in')  # Redirect to sign in page

    
@login_required(login_url='/sign-in/')
def home(request):
    # Access user information using the request object
    user = request.user

    # Fetch incidents from the database
    incidents = Incident.objects.all()

    # Pass user information and incidents to the template context
    context = {'user': user, 'incidents': incidents}
    return render(request, 'home.html', context)


def incident_detail(request, incident_id):
    incident = get_object_or_404(Incident, pk=incident_id)
    comments = Comment.objects.filter(incident=incident)
    context = {'incident': incident, 'comments': comments}
    return render(request, 'incident-detail.html', context)


def report_incident(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            incident = Incident()
            incident.title = form.cleaned_data['title']
            incident.description = form.cleaned_data['description']
            incident.location = form.cleaned_data['location']
            incident.user = request.user
            incident.save()
            return redirect('home')  # Redirect to home page
        else:
            form_errors = form.errors.as_data()
            if '__all__' in form_errors:
                messages.error(request, form_errors['__all__'][0].message)
            else:
                messages.error(request, form_errors)
                
    else:
        form = IncidentForm()
    return render(request, 'report-incident.html', {'form': form})
