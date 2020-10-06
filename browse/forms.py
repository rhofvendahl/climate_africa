from django import forms

SEARCH_TYPE_CHOICES = [
    (None, 'Post type'),
    ('extreme_weather_report', 'Extreme weather report'),
    ('resilience_project', 'Resilience project'),
    ('climate_justice_event', 'Climate justice event'),
    ('well_needed', 'Well needed'),
]

SEARCH_SORT_BY_CHOICES = [
    ('new', 'New'),
    ('recommended', 'Recommended'),
]

class SearchForm(forms.Form):
    query = forms.CharField(required=False, max_length=40)
    city = forms.CharField(required=False, max_length=80)
    type = forms.ChoiceField(required=False, choices=SEARCH_TYPE_CHOICES)
    sort_by = forms.ChoiceField(choices=SEARCH_SORT_BY_CHOICES)

    def clean_city(self):
        city = self.cleaned_data['city']
        if city == 'null':
            return None
        return city
