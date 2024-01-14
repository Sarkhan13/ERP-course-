from django import forms
from .models import teacher,group


class teacher_form(forms.ModelForm):
    class Meta:
        model = teacher

        fields = ('name', 'surname','salary','profession','workpractice','profilepic','techerid','birth','start')

class group_form(forms.ModelForm):
    class Meta:
        model = group

        fields = ('teach', 'name','lesson', 'begin_date', 'lesdays', 'add_info','end_date' )