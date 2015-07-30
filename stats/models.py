from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length=200, unique=True)
    has_death_penalty = models.BooleanField(default=True)
    is_illegal = models.BooleanField(default=True)
    has_employment_protection = models.BooleanField(default=False)
    has_hate_crime_protection = models.BooleanField(default=False)
    has_marriage_recognition = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.country_name