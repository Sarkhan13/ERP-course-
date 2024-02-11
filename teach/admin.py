from django.contrib import admin
from .models import *


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'start')
    search_fields = ('name',)

class StudAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'startdate','payment')
    search_fields = ('name',)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'teach', 'lesson','begin_date')
    search_fields = ('name',)

class JournalAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'rate')
    search_fields = ('student',)

class DateAdmin(admin.ModelAdmin):
    list_display = (  'date_time',)
    search_fields = ('date',)

class TaskAdmin(admin.ModelAdmin):
    list_display = ( 'group', 'title','deadline')
    search_fields = ('group',)


class PayAdmin(admin.ModelAdmin):
    list_display = ( 'student', 'monthly_payment','started_date')
    search_fields = ('student',)


class ChekAdmin(admin.ModelAdmin):
    
    search_fields = ('paymnt',)

admin.site.register(teacher,MemberAdmin)
admin.site.register(group,GroupAdmin)
admin.site.register(student,StudAdmin)
admin.site.register(journal,JournalAdmin)
admin.site.register(date,DateAdmin)
admin.site.register(task,TaskAdmin)
admin.site.register(pay,PayAdmin)
admin.site.register(chek,ChekAdmin)