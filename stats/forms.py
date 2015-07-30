from .models import Country
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Submit', 'Submit', css_class='btn-primary'))