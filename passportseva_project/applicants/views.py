from django.shortcuts import render, redirect
from .models import PassportApplication
from .forms import PassportApplicationForm
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    applications = PassportApplication.objects.filter(user=request.user)
    return render(request, 'applicants/dashboard.html', {'applications': applications})

@login_required
def submit_application(request):
    if request.method == 'POST':
        form = PassportApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect('applicant_dashboard')
    else:
        form = PassportApplicationForm()
    return render(request, 'applicants/submit.html', {'form': form})

@login_required
def edit_application(request, app_id):
    application = PassportApplication.objects.get(id=app_id, user=request.user)
    if application.status != 'PENDING':
        return redirect('applicant_dashboard')
    form = PassportApplicationForm(request.POST or None, instance=application)
    if form.is_valid():
        form.save()
        return redirect('applicant_dashboard')
    return render(request, 'applicants/edit.html', {'form': form})
