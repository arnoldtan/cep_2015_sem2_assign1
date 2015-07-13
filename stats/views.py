from django.shortcuts import render
from django.http import HttpResponse
from .models import Country

# Create your views here.
def index(request):
    allcountries = Country.objects.all()
    return render(request, 'index/index.html', { 'countries': allcountries })

def country(request, country_name):
    allcountries = Country.objects.all()
    country = Country.objects.get(country_name=country_name)
    return render(request, 'country/country.html', { 'countries': allcountries, 'country': country })

def topic(request, topic_name):
    allcountries = Country.objects.all()
    if topic_name == 'has_death_penalty':
        yes = Country.objects.filter(has_death_penalty=True)
        no = Country.objects.filter(has_death_penalty=False)
    elif topic_name == 'has_employment_protection':
        yes = Country.objects.filter(has_employment_protection=True)
        no = Country.objects.filter(has_employment_protection=False)
    elif topic_name == 'has_hate_crime_protection':
        yes = Country.objects.filter(has_hate_crime_protection=True)
        no = Country.objects.filter(has_hate_crime_protection=False)
    elif topic_name == 'has_marriage_recognition':
        yes = Country.objects.filter(has_marriage_recognition=True)
        no = Country.objects.filter(has_marriage_recognition=False)
    elif topic_name == 'is_illegal':
        yes = Country.objects.filter(is_illegal=True)
        no = Country.objects.filter(is_illegal=False)
    numYes = len(yes)
    numNo = len(no)
    return render(request, 'topic/topic.html', {
                                                    'countries': allcountries,
                                                    'topic': topic_name,
                                                    'yes': yes,
                                                    'no': no,
                                                    'numYes': numYes,
                                                    'numNo': numNo
                                                })