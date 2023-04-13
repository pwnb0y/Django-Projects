from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = {'name','dob','gender','locality','city','pin','state','mobile','job_city','profile_pic','my_file'}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'job_city':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':''}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            
        }