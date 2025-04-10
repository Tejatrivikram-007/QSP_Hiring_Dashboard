from django.db import models

class Requirements(models.Model):
    company_id = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    bachelor_degree = models.CharField(max_length=100)
    master_degree = models.CharField(max_length=100, blank=True, null=True) 
    stream = models.CharField(max_length=100)
    percentage = models.FloatField(blank=True,null=True) 
    
    year_of_passout = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    no_of_vacancies = models.IntegerField()
    salary = models.CharField(max_length=100, blank=True, null=True)
    agreement = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company_name} - {self.stream}"

