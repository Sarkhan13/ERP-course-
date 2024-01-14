from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class teacher(models.Model):
    teacher = models.ForeignKey(User, on_delete = models.PROTECT)
    name = models.CharField(max_length = 100, verbose_name = 'müəllimin adı')
    surname = models.CharField(max_length = 100, verbose_name = 'müəllimin soyadı')
    salary = models.IntegerField(verbose_name = 'maaş')
    profession = models.CharField(max_length=100, verbose_name = 'ixtisas')
    workpractice = models.TextField(verbose_name = 'iş təcrubəsi')
    profilepic = models.ImageField(verbose_name='profil şəkli', upload_to='profilepic/')
    techerid = models.IntegerField( verbose_name = 'Müəllim İD-si')
    birth = models.DateTimeField(verbose_name='dogum tarixi', blank=True,null= True)
    start = models.DateTimeField(verbose_name= 'bashlama tarixi', blank=True,null= True)

    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now_add  = True)
    

    def __str__(self):
        return str(self.name)
    
    @property
    def get_url(self):
        return reverse('teachdetail', kwargs={'id':self.id})
    


class group(models.Model):
    teach = models.ForeignKey(teacher,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    lesson = models.CharField(max_length=100)
    begin_date = models.DateTimeField(verbose_name= 'Qrupun dərsə başlama tarixi')
    TYPE = (
        ('B.ertəsi', 'B.ertəsi'),
        ('Ç.axşamı', 'Ç.axşamı'),
        ('Çərşəmbə', 'Çərşəmbə'),
        ('C.axşamı', 'C.axşamı'),
        ('Cümə', 'Cümə'),
        ('C.ertəsi', 'C.ertəsi'),
    )
    lesdays = models.CharField(max_length=100, verbose_name='dərs günü', choices= TYPE )
    add_info = models.TextField(blank=True,null=True, verbose_name='Əlavə məlumat')
    end_date = models.DateTimeField(verbose_name= 'Qrupun bitmə tarixi')

    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.name)


    @property
    def get_url(self):
        return reverse('groupdetail', kwargs={'id':self.id})
