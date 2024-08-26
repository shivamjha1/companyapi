from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=20,choices=(('IT','IT'),('PCO','PCO'),('Retail','Retail')))
    established=models.DateField()
    working=models.BooleanField(default=True)
    about=models.TextField()
    
    def __str__(self) -> str:
        return self.name
    
class Employee(models.Model):
    name=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    salary=models.IntegerField()
    intern=models.BooleanField(default=False)
    company=models.ForeignKey(Company,on_delete=models.CASCADE, null=True,related_name="employees")
    
    def __str__(self) -> str:
        return self.name
    
class PersonalDetails(models.Model):
    address=models.TextField()
    phone=models.IntegerField()
    email=models.EmailField()
    employee=models.OneToOneField(Employee,on_delete=models.CASCADE,null=True)
    