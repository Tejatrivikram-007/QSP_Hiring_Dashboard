from django import forms
from .models import Requirements

class RequirementForm(forms.ModelForm):
    class Meta:
        model = Requirements
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RequirementForm, self).__init__(*args, **kwargs)
        
        self.fields['company_id'].widget.attrs['placeholder'] = 'Enter Company ID'
        self.fields['company_name'].widget.attrs['placeholder'] = 'Enter Company Name'
        self.fields['bachelor_degree'].widget.attrs['placeholder'] = 'e.g., B.Tech, B.Sc'
        self.fields['master_degree'].widget.attrs['placeholder'] = 'e.g., MCA'
        self.fields['stream'].widget.attrs['placeholder'] = 'Enter Stream (e.g., CSE, ECE)'
        self.fields['percentage'].widget.attrs['placeholder'] = 'Minimum Percentage Required'
        self.fields['year_of_passout'].widget.attrs['placeholder'] = 'e.g., 2024'
        self.fields['salary'].widget.attrs['placeholder'] = 'e.g., 500000'
        self.fields['agreement'].widget.attrs['placeholder'] = 'Mention (if any) e.g., 1.6 yrs (18 months)'
        self.fields['location'].widget.attrs['placeholder'] = 'Job Location'
        self.fields['no_of_vacancies'].widget.attrs['placeholder'] = 'Number of Openings'
