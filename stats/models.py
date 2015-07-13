from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length=200)
    has_death_penalty = models.BooleanField()
    is_illegal = models.BooleanField()
    has_employment_protection = models.BooleanField()
    has_hate_crime_protection = models.BooleanField()
    has_marriage_recognition = models.BooleanField()
    
    def __unicode__(self):
        return self.country_name