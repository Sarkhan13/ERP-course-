from django import forms
from .models import teacher,group,student,task,pay


class teacher_form(forms.ModelForm):
    class Meta:
        model = teacher

        fields = ('name', 'surname','salary','profession','workpractice','profilepic','techerid','birth','start')

class group_form(forms.ModelForm):
    class Meta:
        model = group

        fields = ('teach', 'name','lesson', 'begin_date', 'lesdays', 'add_info','end_date' )




class student_form(forms.ModelForm):
    class Meta:
        model = student

        fields = ('user', 'group', 'name', 'surname','birthday', 'startdate', 'payment', 'profilepic')



class task_form(forms.ModelForm):
    class Meta:
        model = task

        fields = ('teacher','group','title', 'text', 'deadline', 'rate')



class pay_form(forms.ModelForm):
    class Meta:
        model = pay

        fields = ('student','monthly_payment','started_date','ended_date','note','sale')