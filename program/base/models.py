from unicodedata import name
from django.db import models

# Create your models here.

class User6(models.Model):
    image_id = models.IntegerField(db_column='imageid')
    name = models.CharField(max_length=45)   
    birthday = models.CharField(max_length=45, default = True)
    sex = models.CharField(max_length=45, default = True)
    height = models.FloatField(default = True)


    def __str__(self):
        return self.name
    
    #class Meta:
    #    db_table = 'tb_user'

#def set_globvar_to_one():
#    global height
#    height = User6.height

'''
user = User6.objects.get(name='test')
height = user.height
height = User6.objects.get(name='test').height
'''
class Data6(models.Model):
    #userid = models.IntegerField(db_column='userid', default = True)
    #name = models.CharField(max_length=45) 
    userid = models.ForeignKey(User6, on_delete=models.CASCADE,default = False)#SET_NULL,null=True  
    #names = models.CharField(max_length=45,default = True)
    weight = models.FloatField(default = True) 
    temperature = models.FloatField(default = True)
    pressures = models.IntegerField(default = True)
    pressured = models.IntegerField(default = True)
    bmi = models.FloatField(default = 0.0)
    bmr = models.FloatField(default=0.0)
    result1 = models.CharField(max_length=100,default = True)
    result2 = models.CharField(max_length=100,default = True)
    result3 = models.CharField(max_length=100,default = True)

    '''
    #from .models import User6
    #height = User6.objects.get(userid=name).height
    #set_globvar_to_one()
    #(BMI)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        height_m = self.temperature / 100  
        self.bmi = self.weight / (height_m ** 2)
    
    def __init__(self, *args, **kwargs):
        user = User6.objects.get(name='userid')
        super().__init__(*args, **kwargs)
        height = user.height
        height_m = self.height / 100  
        self.bmi = self.weight / (height_m ** 2)
    
    #def __init__(self, *args, **kwargs):
    #    users = User6.objects.all().values('userid', 'height')


    def __str__(self):
        return self.userid
    
    
    class Meta:
        db_table = 'tb_data'
    '''   


class test(models.Model):
    x = models.FloatField(default = 100.0)
    y = models.FloatField(default = 2.0)
    z = models.FloatField(default = 0.0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        height_m = self.x / 100 
        self.z = self.y / (height_m ** 2)
'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.z = self.x * self.y
'''
