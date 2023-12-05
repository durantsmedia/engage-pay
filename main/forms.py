from django import forms 
  
# creating a form 
class ParentForm(forms.Form): 
    email = forms.CharField(label='Your Email Address') 
    phone = forms.CharField(label='Phone No. +254XXXxxxxxx', required=False) 
    invoice = forms.IntegerField(label='Invoice Number')  
