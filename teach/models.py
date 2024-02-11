from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class teacher(models.Model):
    user = models.ForeignKey(User,related_name='teacher_user', on_delete = models.PROTECT,default=1)
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
    teach = models.ForeignKey(teacher,on_delete=models.PROTECT)
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
    



class student(models.Model):
    user = models.ForeignKey(User,related_name='student_user', on_delete=models.CASCADE, default=1)
    group = models.ForeignKey(group, on_delete=models.PROTECT,verbose_name='Yazıldığı qrup')
    name = models.CharField(max_length=100, verbose_name= 'Tələbənin adı')
    surname = models.CharField(max_length=100, verbose_name = 'soyadı')
    birthday = models.DateField(verbose_name = 'təvəllüdü')
    startdate = models.DateTimeField(verbose_name = 'qrupa başlama tarixi')
    payment = models.IntegerField(verbose_name = 'Aylıq ödəniş(AZN)')
    profilepic = models.ImageField(verbose_name='profil şəkli')

    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.name)
    
    @property
    def get_url(self):
        return reverse('stud_panel', kwargs={'id':self.id})
    



class date(models.Model): 
    group = models.ForeignKey(group, on_delete=models.CASCADE, verbose_name='qrupun adı')
    date_time = models.DateField(verbose_name='tarix')

    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f'{self.date_time} {self.group.name}' 




class journal(models.Model):
    date = models.ForeignKey(date, on_delete=models.PROTECT, verbose_name='tarix', blank=True, null=True)
    student = models.ForeignKey(student, on_delete=models.CASCADE,verbose_name='Tələbə')
    rate = models.IntegerField(verbose_name='qiymət',blank=True, null=True)
    existence = models.BooleanField(default = True, verbose_name='davamiyyət')

    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.student.name)



class task(models.Model):
    teacher = models.ForeignKey(teacher, on_delete=models.PROTECT, verbose_name='Taskın müəllimi')
    group = models.ForeignKey(group, on_delete=models.CASCADE,verbose_name='qrup')
    title = models.CharField(max_length=200, verbose_name='başlıq')
    text = models.TextField(verbose_name='mətn')
    deadline = models.DateField(verbose_name='bitmə tarixi')
    rate = models.IntegerField(verbose_name='qiymət',blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.title} {self.group.name}'
    

    @property
    def get_url(self):
        return reverse('task_detail', kwargs={'id':self.id})
    



class pay(models.Model):
    student = models.ForeignKey(student, on_delete=models.PROTECT, blank=True, null=True)
    monthly_payment = models.IntegerField(verbose_name='aylıq ödəniş',blank=True, null=True)
    started_date = models.DateField(verbose_name='kursa başlama tarixi',blank=True, null=True)
    ended_date = models.DateField(verbose_name='kursu bitirəcəyi tarix',blank=True, null=True)
    note = models.TextField(verbose_name='qeyd',blank=True, null=True)
    sale = models.IntegerField(verbose_name='endirim', blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.student.name)
    


class chek(models.Model):
    paymnt = models.ForeignKey(pay, on_delete = models.CASCADE, verbose_name = 'ödəniş', related_name='cheks')
    payment_date = models.DateField(verbose_name= 'ödəməli olduğu son tarix',blank=True, null=True)
    payed = models.BooleanField(verbose_name= 'ödənildi',default=False,blank=True, null=True) 

    created_date = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now_add = True,blank=True, null=True) 

    def __str__(self):
        return f'{self.paymnt.student.name} {self.payment_date}' 

    @property
    def get_url(self):
        return reverse('chek_update', kwargs={'id':self.id}) 




