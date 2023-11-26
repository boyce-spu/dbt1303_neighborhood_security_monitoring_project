from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up, name='sign-up'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-out/', views.sign_out, name='sign-out'),
    path('home/', views.home, name='home'),
    path('incident/<int:incident_id>/', views.incident_detail, name='incident_detail'),
    path('report-incident/', views.report_incident, name='report-incident'),
]
