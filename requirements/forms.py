from django import forms
from .models import Requirements,Schedule

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
        self.fields['skills'].widget.attrs['placeholder'] = 'Mention (if any) e.g.'
        self.fields['location'].widget.attrs['placeholder'] = 'Job Location'
        self.fields['no_of_vacancies'].widget.attrs['placeholder'] = 'Number of Openings'

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)

        self.fields['company_name'].widget.attrs['placeholder'] = 'Enter Company Name'
        self.fields['company_address'].widget.attrs['placeholder'] = 'Enter Address (optional)'
        self.fields['company_location'].widget.attrs['placeholder'] = 'Enter Location (e.g., Bangalore)'
        self.fields['requirement_id'].widget.attrs['placeholder'] = 'Enter Requirement ID (e.g., REQ001)'
        self.fields['students_name'].widget.attrs['placeholder'] = 'Enter comma-separated names (e.g., Teja Trivikram, Rajesh Koundinya)'