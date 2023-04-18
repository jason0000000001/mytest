from unicodedata import name
from django.db import models
import django.utils.timezone as timezone

# Create your models here.

class User6(models.Model):
    image_id = models.IntegerField(db_column='imageid')#圖片id
    name = models.CharField(max_length=45)#姓名
    birthday = models.CharField(max_length=45, default = True)#出生年月日
    sex = models.CharField(max_length=45, default = True)#性別
    height = models.FloatField(default = True)#身高
    createtime = models.DateTimeField(auto_now_add = timezone.now)#創建時間
    #updatetime = models.DateTimeField(auto_now = True)#更新時間


    def __str__(self):
        return self.name
    
    #class Meta:
    #    db_table = 'tb_user'


class Data6(models.Model):
    #userid = models.IntegerField(db_column='userid', default = True)
    #name = models.CharField(max_length=45) 
    userid = models.ForeignKey(User6, on_delete=models.CASCADE,default = False)#使用者id 
    weight = models.FloatField(default = True) #體重
    temperature = models.FloatField(default = True)#體溫
    pressures = models.IntegerField(default = True)#收縮壓
    pressured = models.IntegerField(default = True)#舒張壓
    heartbeat = models.IntegerField(default = 0)#心跳
    bmi = models.FloatField(default = 0.0)#bmi
    bmr = models.FloatField(default=0.0)#bmr
    result1 = models.CharField(max_length=100,default = True)#血壓建議
    result2 = models.CharField(max_length=100,default = True)#體溫建議
    result3 = models.CharField(max_length=100,default = True)#心跳建議
    result4 = models.CharField(max_length=100,default = True)#BMI建議
    createtime = models.DateTimeField(auto_now_add = timezone.now)#創建時間
    #updatetime = models.DateTimeField(auto_now = True)#更新時間

    #def __str__(self):
    #    return self.userid

    
    '''
    #from .models import User6
    #height = User6.objects.get(userid=name).height
    #set_globvar_to_one()
    #(BMI)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        height_m = self.temperature / 100  
        self.bmi = self.weight / (height_m ** 2)


    class Meta:
        db_table = 'tb_data'
    '''   


class Medicine(models.Model):
    userid = models.ForeignKey(User6, on_delete=models.CASCADE,default = False)#使用者id 
    medicine = models.TextField(null=True)


    def __str__(self):
        return self.medicine
    


class test(models.Model):
    x = models.FloatField(default = 100.0)
    y = models.FloatField(default = 2.0)
    z = models.FloatField(default = 0.0)
    cdate = models.DateTimeField(auto_now_add=timezone.now)
    udate = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        height_m = self.x / 100 
        self.z = self.y / (height_m ** 2)

    #def __str__(self):
    #    return self.cdate

'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.z = self.x * self.y
'''
