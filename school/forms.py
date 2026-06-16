from django import forms
from school.models import Student

class StudentForm(forms.ModelForm):
    address = forms.CharField(widget=forms.NumberInput(attrs={'placeholder':"Enter the address","class":"form-control"}))
    dob = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))

    class Meta:
        model = Student
        fields = '__all__'