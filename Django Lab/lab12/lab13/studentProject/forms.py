from django import forms
from.models import student


class stdForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ('std_name', 'std_rollno', 'std_contact', 'project_title')