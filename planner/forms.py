from django import forms
from django.contrib.auth.models import User

from planner.models import Profile, Major_option, School_option


class LoginForm(forms.Form):
    id_number = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'ID Number',
                                    'class': 'form-control'}), required=True)

    password = forms.CharField(max_length=25,
                               widget=forms.PasswordInput(attrs={
                                   'placeholder': 'Password',
                                   'class': 'form-control'}), required=True)

Semester_enrolled = (
    ('spring', 'Spring'),
    ('fall', 'Fall'))


class RegisterForm(forms.Form):
    firstname = forms.CharField(max_length=25)
    lastname = forms.CharField(max_length=25)
    email = forms.CharField(max_length=25)
    school = forms.CharField(max_length=25)
    password = forms.CharField(max_length=25,widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_again = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password_again']

class Student_enroll_profile_Form(forms.ModelForm):
    semester_enrolled = forms.ChoiceField(choices=Semester_enrolled)
    year_enrolled = forms.ChoiceField(choices=list(zip(range(2010, 2025), range(2010, 2025))))
    major = forms.ModelChoiceField(queryset=Major_option.objects.all())
    school = forms.ModelChoiceField(queryset=School_option.objects.all())

    class Meta:
        model = Profile
        fields = ["semester_enrolled", "year_enrolled", "major", "school"]

class MyForm(forms.Form):
    checkbox = forms.BooleanField(required=False)
