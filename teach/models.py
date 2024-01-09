from django.db import models

from django.contrib.auth.models import User


class teacher(models.Model):
    teacher = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100, verbose_name = 'müəllimin adı')
    surname = models.CharField(max_length = 100, verbose_name = 'müəllimin soyadı')
    birthday = models.IntegerField(verbose_name = 'təvəllüdü')
    startdate = models.IntegerField(verbose_name = 'işə başladığı tarix')
    salary = models.IntegerField(verbose_name = 'maaş')
    profession = models.CharField(max_length=100, verbose_name = 'ixtisas')
    workpractice = models.TextField(verbose_name = 'iş təcrubəsi')
    profilepic = models.ImageField(verbose_name='profil şəkli')
    techerid = models.IntegerField( verbose_name = 'Müəllim İD-si')

    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now_add  = True)
    

    def __str__(self):
        return str(self.name)