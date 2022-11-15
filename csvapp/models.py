from django.db import models

# Create your models here.


class Csv_emp(models.Model):
    name = models.CharField(max_length = 100) 
    company = models.CharField(max_length = 100)
    salary = models.IntegerField()
    designation = models.CharField(max_length = 100)
    DOJ = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = True)

    def __str__(self):
        return f'{self.name}---------{self.company}'
    
    class Meta:
        db_table = 'emp'


class Employee(models.Model):
    Emp_Name = models.CharField(max_length=200)
    Emp_Salary = models.IntegerField()
    is_boolean = models.BooleanField(default=True)
    Emp_company = models.CharField(max_length=200)

    
    def __str__(self):
        return f"{self.Emp_Name} -- {self.Emp_company}"

    class Meta:
        db_table = "empl"














    # def delete(self,*args,**kwargs):
    #     self.pdf.delete()
    #     self.cover.delete()
    #     super().delete(*args,**kwargs)

    
