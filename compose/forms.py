from django import forms
from django.forms.widgets import TextInput, Textarea, ClearableFileInput, SelectDateWidget
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

POST_TYPE_CHOICES = [
    (None, 'Post type (select one)'),
    ('extreme_weather_report', 'Extreme weather report'),
    ('resilience_project', 'Resilience project'),
    ('climate_justice_event', 'Climate justice event'),
    ('well_needed', 'Well needed'),
]

class PostForm(forms.Form):
    title = forms.CharField(widget=TextInput(attrs={'placeholder': 'Title'}))
    text = forms.CharField(widget=Textarea(attrs={'placeholder': 'Text'}))
    city = forms.CharField(max_length=80)
    # image = forms.ImageField(widget=ClearableFileInput(attrs={'class': 'form-control-file'}))
    image = forms.ImageField(required=False)
    type = forms.ChoiceField(choices=POST_TYPE_CHOICES)

    report_type = forms.CharField(max_length=40, required=False) # selectivity single -> tag
    report_impacts = forms.CharField(max_length=800, required=False) # selectivity multiple -> tags
    project_intentions = forms.CharField(max_length=800, required=False) # selectivity multiple -> tags
    # event_date = forms.DateField(required=False, initial=datetime.date.today)
    event_date = forms.DateField(required=False, widget=SelectDateWidget())
    well_amount = forms.IntegerField(required=False, min_value=0)
    well_population = forms.IntegerField(required=False, min_value=0)

    def clean_city(self):
        city = self.cleaned_data['city']
        if (not city) or (city == 'null'):
            self.add_error('city', ValidationError('Please select a city from the dropdown'))
        return city

    def clean_type(self):
        type = self.cleaned_data['type']
        if not type:
            self.add_error('type', ValidationError('Please select a post type from the dropdown'))
        return type

    def clean_report_type(self):
        type = self.cleaned_data['type']
        report_type = self.cleaned_data['report_type']
        # print('CLEANED DATA IN FORM', self.cleaned_data)
        # print('REPORT_TYPE', report_type)
        if (not report_type) or (report_type == 'null'):
            if type == 'extreme_weather_report':
                self.add_error('report_type', ValidationError('Please select an extreme weather type from the dropdown'))
            else:
                return None
        return report_type

    def clean_report_impacts(self):
        type = self.cleaned_data['type']
        report_impacts = self.cleaned_data['report_impacts']
        if (not report_impacts) or (report_impacts == 'null'):
            return None
        return report_impacts

    def clean_project_intentions(self):
        type = self.cleaned_data['type']
        project_intentions = self.cleaned_data['project_intentions']
        if (not project_intentions) or (project_intentions == 'null'):
            return None
        return project_intentions

    def clean_event_date(self):
        type = self.cleaned_data['type']
        event_date = self.cleaned_data['event_date']
        if type == 'climate_justice_event':
            if not event_date:
                self.add_error('event_date', ValidationError('Please select an event date'))
        return event_date

    def clean_well_amount(self):
        type = self.cleaned_data['type']
        well_amount = self.cleaned_data['well_amount']
        if type == 'well_needed':
            if not well_amount:
                self.add_error('well_amount', ValidationError('Please enter how much the well will cost (USD)'))
        return well_amount

    def clean_well_population(self):
        type = self.cleaned_data['type']
        well_population = self.cleaned_data['well_population']
        if type == 'climate_justice_event':
            if not well_population:
                self.add_error('well_population', ValidationError('Please enter how many people the well will serve'))
        return well_population
