from django.db import models
from django.contrib.auth.models import User

class PassportApplication(models.Model):
    STATUS_CHOICES = [('PENDING', 'Pending'), ('UNDER_REVIEW', 'Under Review'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    nationality = models.CharField(max_length=50)
    aadhar_number = models.CharField(max_length=12, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    submission_date = models.DateTimeField(auto_now_add=True)
