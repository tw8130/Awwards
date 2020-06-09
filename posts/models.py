from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save 
from django.dispatch import receiver
import numpy as np
from django.db.models import Avg, Max, Min
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = HTMLField()
    link = models.CharField(max_length=100)
    # user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="project")
    image = models.ImageField(upload_to='project_pics',blank=True)
    design = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    usability = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    content = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    vote_submissions = models.IntegerField(default=0)


    # def average_design(self):
    #     design_ratings = list(map(lambda x: x.design_rating, self.reviews.all()))
    #     return np.mean(design_ratings)

    # def average_usability(self):
    #     usability_ratings = list(map(lambda x: x.usability_rating, self.reviews.all()))
    #     return np.mean(usability_ratings)

    # def average_content(self):
    #     content_ratings = list(map(lambda x: x.content_rating, self.reviews.all()))
    #     return np.mean(content_ratings)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
    
    def save_project(self):
        self.save()

    @classmethod
    def fetch_all_images(cls):
        all_images = Project.objects.all()
        return all_images
    
    @classmethod
    def get_single_project(cls, project):
        project = cls.objects.get(id=project)
        return project

    @classmethod
    def search_project_by_title(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project
    
    @classmethod
    def delete_project_by_id(cls, id):
        projects = cls.objects.filter(pk=id)
        projects.delete()

    @classmethod
    def get_project_by_id(cls, id):
        projects = cls.objects.get(pk=id)
        return projects

    @classmethod
    def update_project(cls, id):
        projects = cls.objects.filter(id=id).update(id=id)
        return projects

    @classmethod
    def update_description(cls, id):
        projects = cls.objects.filter(id=id).update(id=id)
        return projects


class Profile(models.Model):
    profile_picture = models.ImageField(upload_to='prof_pics/',blank=True)
    prof_user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    bio = models.TextField()
    all_projects=models.ForeignKey(Project, null=True,on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return f'{self.prof_user.username}.Profile'
    
    #create user
    # @receiver(post_save, sender=User,dispatch_uid='save_new_user_profile',) 
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)

    
    # #save user
    # @receiver(post_save, sender=User) 
    # def save_user_profile(sender, instance, **kwargs):
    #     user_profile = UserProfile.objects.get(user=instance)
    #     user_profile.save()
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

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

    def save_comment(self):
        self.save()

    def get_comment(self, id):
        comments = Review.objects.filter(image_id =id)
        return comments

    def __str__(self):
        return self.comment

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()