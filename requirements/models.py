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
    skills = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company_name} - {self.stream}"


class Schedule(models.Model):
    requirement_id = models.CharField(max_length=35,blank=True)    
    company_name = models.CharField(max_length=100)
    company_location = models.CharField(max_length=100,null=True,blank=True)
    company_address = models.CharField(max_length=500,null=True,blank=True)
    students_name = models.TextField()
    
    def studentslist(self):
        return self.students_name.split(',')
    
    def _str_(self):
        return f"{self.requirement_id} - {self.company_name} - {self.company_location} - {self.company_address} - {self.students_name}"


