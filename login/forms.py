from django import forms

class Myform(forms.Form):
    rollno=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)
    confirmpassword=forms.CharField(max_length=100)