from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['id', 'name', 'dob', 'gender', 'locality',
            'email', 'city', 'pin', 'state', 'mobile', 'job_city', 'profile_image', 'my_file'
        ]