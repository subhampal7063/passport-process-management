from django.shortcuts import render, redirect
from applicants.models import PassportApplication
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def review_applications(request):
    applications = PassportApplication.objects.all()
    return render(request, 'admins/review.html', {'applications': applications})

@staff_member_required
def update_status(request, app_id, status):
    app = PassportApplication.objects.get(id=app_id)
    app.status = status
    app.save()
    return redirect('admin_review')

@staff_member_required
def export_csv(request):
    import csv
    from django.http import HttpResponse

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="passport_applications.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Aadhar', 'Status', 'Submission Date'])
    for app in PassportApplication.objects.all():
        writer.writerow([app.id, app.full_name, app.aadhar_number, app.status, app.submission_date])

    return response
