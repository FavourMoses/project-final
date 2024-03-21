from django.contrib import admin
from . models import Requisition

@admin.register(Requisition)
class RequisitionAdmin(admin.ModelAdmin):
    display = ['Name', 'Categories', 'Purpose'] 

# admin.site.register(Approval)