from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save 
from django.dispatch import receiver
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = HTMLField()
    link = models.CharField(max_length=100)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,relatedname=)
    image = models.ImageField(upload_to='project_pics',blank=True)
    design = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    usability = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    content = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    vote_submissions = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

class Profile(models.Model):
    profile_picture = models.ImageField(upload_to='prof_pics/',blank=True)
    prof_user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    bio = models.TextField()
    contact_info = models.CharField(max_length=200,blank=True)
    all_projects = models.ForeignKey('Project',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.user.username}.Profile'
