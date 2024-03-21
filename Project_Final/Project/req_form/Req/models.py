from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Requisition(models.Model):
    CHOICES = [
    ('Office supplies', 'OFFICE SUPPLIES'),
    ('Salaries', "SALARIES"),
    ('Minor_repairs', "MINOR REPAIRS"),
    ('Resource_persons', "RESOURCE PERSONS"),
    ('Project_funding', "PROJECT FUNDING")
    ] 
    Categories = models.TextField(choices=CHOICES, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Phone_number = models.IntegerField()
    Bank_name = models.TextField(max_length=20)
    Account_number = models.IntegerField()
    Item_name = models.TextField(max_length=50)
    Purpose = models.CharField(max_length=70)
    Amount = models.IntegerField()
    Date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    rd = ['Approved', 'Unapproved']

    def get_absolute_url(self):
        return reverse('Req:requisition')

    class Meta:
        verbose_name_plural = 'Requisitions'
        ordering = ['-Date']
        permissions = [
            ("can_approve_requisition", "Can approve requisitions"),
            ("can_reject_requisition", "Can reject requisitions"),
        ]

    def __str__(self):
        return f"{self.user} -- {self.Categories}"
    
