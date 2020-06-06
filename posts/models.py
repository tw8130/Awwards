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
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="project")
    image = models.ImageField(upload_to='project_pics',blank=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

class Profile(models.Model):
    profile_picture = models.ImageField(upload_to='prof_pics/',blank=True)
    prof_user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    bio = models.TextField()
    contact_info = models.CharField(max_length=200,blank=True)
    all_projects = models.ForeignKey(Project,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.user.username}.Profile'

    #create user
    @receiver(post_save, sender=User) 
    def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
    #save user
    @receiver(post_save, sender=User) 
    def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),

    )
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    design_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    usability_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    content_rating = models.IntegerField(choices=RATING_CHOICES, default=0)

    def __str__(self):
        return self.comment