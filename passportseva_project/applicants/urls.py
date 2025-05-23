from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='applicant_dashboard'),
    path('submit/', views.submit_application, name='submit_application'),
    path('edit/<int:app_id>/', views.edit_application, name='edit_application'),
]
