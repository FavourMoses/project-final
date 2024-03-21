from django import forms
from .models import Requisition

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RequisitionForm(forms.ModelForm):
    class Meta:
        model = Requisition
        fields = ['Categories', 'Phone_number', 'Amount', 'Bank_name', 'Account_number', 'Item_name','Purpose']
        widgets = {
            'Categories': forms.Select(attrs={'style': 'width: 300px; margin-right:40px'}),
            'Phone_number': forms.TextInput(attrs={'style': 'width: 300px; margin-right:40px'}),
            'Amount' : forms.TextInput(attrs={'style': 'width: 300px; margin-right:40px'}),
            'Bank_name': forms.TextInput(attrs={'style': 'width: 300px; margin-right:40px'}),
            'Account_number': forms.TextInput(attrs={'style': 'width: 300px; margin-right:40px'}),
            'Item_name': forms.TextInput(attrs={'style': 'width: 300px; margin-right:40px'}),
            'Purpose': forms.Textarea(attrs={'style': 'width: 300px; height: 150px; margin-right:40px'}),
        }
    
    Purpose = forms.CharField(required=False)
    
class ApprovalForm(forms.ModelForm):
    class Meta:
        model = Requisition
        fields = ['approved']
