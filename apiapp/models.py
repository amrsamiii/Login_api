from django.db import models

# Create your models here.
class awsimage(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField('images/',default="")

# class test(models.Model):
#     title=models.CharField(max_length=50)

class Diseases(models.Model):
    name=models.CharField(max_length=30)
    on = models.ForeignKey('Fertilizers',blank=True,null=True,on_delete=models.CASCADE)

    

class Fertilizers(models.Model):
    name=models.CharField(max_length=64)
    Diseases=models.ForeignKey(Diseases,null=True,on_delete=models.DO_NOTHING)

