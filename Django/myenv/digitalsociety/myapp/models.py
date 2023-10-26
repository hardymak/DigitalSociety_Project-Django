from django.db import models

# Create your models here.
""" 
                        User 
                         |
                         V
                         
                         
                        Email
                        Passworld
                        Role
                         |
                         V
        ----------------------------------
        |                                |
        V                                V
    Chairman                      Society Member
                  
"""

class User(models.Model):
    email = models.EmailField(unique=True,max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30)

    def __str__(self):
        return self.email

class Chairman(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contactno = models.CharField(max_length=30)
    pic = models.FileField(upload_to="media/images", default="media/default.avif")
    
    def __str__(self):
        return self.firstname
    

class SocietyMember(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contactno = models.CharField(max_length=30)    
    no_of_familymember = models.CharField(max_length=30)
    house_no = models.CharField(max_length=10)
    vehicle_details = models.CharField(max_length=30)
    no_of_vehicle = models.CharField(max_length=10)
    occupation = models.CharField(max_length=30)
    job_address = models.CharField(max_length=100,blank=True,null=True)
    area_code = models.CharField(max_length=10)
    pic = models.FileField(upload_to="media/images",default="media/default.avif")
    
class Notice(models.Model):
    notice_title = models.CharField(max_length=50)
    notice_description = models.TextField()
    pic = models.FileField(upload_to="media/images",null=True,blank=True)
    video = models.FileField(upload_to="media/video",null=True,blank=True)
    
 