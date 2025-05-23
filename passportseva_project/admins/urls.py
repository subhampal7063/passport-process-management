from django.urls import path
from . import views

urlpatterns = [
    path('review/', views.review_applications, name='admin_review'),
    path('update/<int:app_id>/<str:status>/', views.update_status, name='update_status'),
    path('export/', views.export_csv, name='export_csv'),
]
