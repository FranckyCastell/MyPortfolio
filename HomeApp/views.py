from django.shortcuts import render
from HomeApp.models import Education, Experience, Award

# Create your views here.


def home(request):
    educations = Education.objects.all().order_by('-title')
    experiences = Experience.objects.all().order_by('-dateEnd')
    awards = Award.objects.all().order_by('title')

    context = {'educations': educations,
               'experiences': experiences, 'awards': awards}
    return render(request, 'HomeApp/home.html', context)
