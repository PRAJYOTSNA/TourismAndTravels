from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
              
class Profile(models.Model):
          user = models.OneToOneField(User,on_delete = models.CASCADE,primary_key = True)
          fname = models.CharField(max_length = 200)
          lname = models.CharField(max_length = 50, null=True, blank=True, default=None)
          address = models.CharField(max_length = 100, null=True, blank=True, default=None)
          phone = models.IntegerField(null=True, blank=True, default=None)
          email = models.EmailField()
          
@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
       if created:
           Profile.objects.create(user = instance)

@receiver(post_save, sender = User)
def  save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    
    
class State(models.Model):
          state=models.CharField(max_length=100)
          image = models.CharField(max_length = 100, default = None, null = True)
          def __str__(self):
                 return str(self.state)
                 
class City(models.Model):
          city=models.CharField(max_length=100)
          
          def __str__(self):
                 return str(self.city)

class Area(models.Model):
          area=models.CharField(max_length=100)
          
          def __str__(self):
                 return str(self.area)
                 
class PlaceMap(models.Model):
          stateid=models.ForeignKey(State)
          cityid=models.ForeignKey(City)
          areaid=models.ForeignKey(Area)
          
          def __str__(self):
                 #return "{0}-{1}-{2}".format(self.stateid,self.cityid,self.areaid) 
                 return str(self.areaid)
                 


class Packages(models.Model):
          mapid = models.ForeignKey(PlaceMap)
          stateid = models.ForeignKey(State)
          image = models.CharField(max_length = 150, default = None, null = True)
          description = models.CharField(max_length = 1000)
          no_of_days = models.IntegerField()
          ratings = models.FloatField(null = True, blank = True, default = None)
          category = models.CharField(max_length = 30)
          travelling_charges = models.IntegerField(null = True, blank = True, default = None)
          def __str__(self):
                 return str(self.mapid)
                 
class Amount(models.Model):
          packageid = models.ForeignKey(Packages)
          stay = models.IntegerField()
          food = models.IntegerField()
          travelling_charges = models.IntegerField()
          offer_price = models.IntegerField()
          
          def __str__(self):
                 return str(self.packageid)
                 
class Booking(models.Model):
          userid=models.ForeignKey(User)
          packageid=models.ForeignKey(Packages)
          travelling_date = models.CharField(max_length = 10)
          amount = models.IntegerField()
          no_of_persons = models.IntegerField()
          
          def __str__(self):
                 return str(self.userid)
                 
                 
class Rating(models.Model):
          userid=models.ForeignKey(User)
          packageid=models.ForeignKey(Packages)
          rating = models.FloatField()
          
          def __str__(self):
                 return str(self.rating)

