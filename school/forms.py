from django import forms
from school.models import Student, Subject,Grade,Teacher

class StudentForm(forms.ModelForm):
    address = forms.CharField(widget=forms.NumberInput(attrs={'placeholder':"Enter the address","class":"form-control"}))
    dob = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))

    class Meta:
        model = Student
        fields = '__all__'


class SubjectForm(forms.ModelForm):
    name = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Enter subject name','class': 'form-control' }) )
    short_name = forms.CharField(required=False, widget=forms.TextInput(attrs={ 'placeholder': 'Enter short name','class': 'form-control' }))

    class Meta:
        model = Subject
        fields = '__all__'

class GradeForm(forms.ModelForm):
    name = forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder': 'Enter grade name','class': 'form-control'}))
    class_teacher = forms.ModelChoiceField( queryset=Teacher.objects.all(),widget=forms.Select(attrs={'class': 'form-select'}))
    subject = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(), required=False,widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Grade
        fields = '__all__'