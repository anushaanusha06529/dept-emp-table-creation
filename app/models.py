from django.db import models

# Create your models here.
class Dept(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)



class Emp(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Dept, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    job=models.CharField(max_length=90)
    comm=models.DecimalField(max_digits=5,decimal_places=2)
    hiredate=models.DateField(auto_now=True)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)