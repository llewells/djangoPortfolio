from django.shortcuts import render
from .models import Job


def home(request):
    jobs = Job.objects # pulls in all the job objectes
    return render(request, 'jobs/home.html', {'jobs':jobs})
