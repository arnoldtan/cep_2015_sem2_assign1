from django.views.generic import View
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .forms import CountryForm
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import Country

# Create your views here.
class CountryCreate(CreateView):
    model = Country
    form_class = CountryForm

class CountryUpdate(UpdateView):
    model = Country
    form_class = CountryForm

class CountryDelete(DeleteView):
    model = Country

# API
class ApiCountryAll(View):
    def get(self, request):
        allcountries = serializers.serialize("json", Country.objects.all())
        return JsonResponse(allcountries, safe=False)


class IndexView(View):
    def get(self, request):
        allcountries = Country.objects.all()
        return render(request, 'index/index.html', { 'countries_list': allcountries })

class CountryView(View):
    def get(self, request, country_name):
        allcountries = Country.objects.all()
        country = Country.objects.get(country_name=country_name)
        return render(request, 'country/country.html', {
                'countries_list': allcountries, 'country': country
            })

class TopicView(View):
    def get(self, request, topic_name):
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
                                                        'countries_list': allcountries,
                                                        'topic': topic_name,
                                                        'yes': yes,
                                                        'no': no,
                                                        'numYes': numYes,
                                                        'numNo': numNo
                                                    })