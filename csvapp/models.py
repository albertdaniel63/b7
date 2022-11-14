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














    # def delete(self,*args,**kwargs):
    #     self.pdf.delete()
    #     self.cover.delete()
    #     super().delete(*args,**kwargs)

    
