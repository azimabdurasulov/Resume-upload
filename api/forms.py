from django import forms
from .models import Resume

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

JOB_CITY_CHOICES = [
    ('Samarkand', 'Samarkand'),
    ('Toshkent', 'Toshkent'),
    ('Navoiy', 'Navoiy'),
    ('Buxoro', 'Buxoro'),
    ('Andijon', 'Andijon'),
    ('Xorazm', 'Xorazm'),
    ('Sirdaryo', 'Sirdaryo'),
    ('Surxondaryo', 'Surxondaryo'),
    ('Fargona', 'Fargona'),
    ('Namangan', 'Namangan'),
    ('Qashqadaryo', 'Qashqadaryo'),
]

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preffered Job Locations',
        choices=JOB_CITY_CHOICES, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = ['id', 'name', 'dob', 'gender', 'locality',
            'email', 'city', 'pin', 'state', 'mobile', 'job_city', 'profile_image', 'my_file'
        ]

        labels = {
            'name': 'Full name',
            'dob': 'Date of Birth',
            'email': 'Email Id',
            'pin': 'Pin Code', 
            'mobile': 'Mobile No',
            'profile_image': 'Profile Image',
            'my_file': 'Document',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'class':'form-control'}),
            'locality': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'pin': forms.NumberInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class':'form-select'}),
            'mobile': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }