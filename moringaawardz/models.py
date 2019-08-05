from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save

# Create your models here.

        
class Project(models.Model):
    title = models.CharField(max_length =60)
    description = HTMLField()
    link = models.CharField(max_length =60)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    projimage = models.ImageField(upload_to = 'articles/', blank=True)


    def __str__(self):
        return self.title
    
    
    @classmethod
    def get_projects(cls):
        projos = cls.objects.all()
        return projos


    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects


    def delete_project(self):
        self.delete()       

    def save_project(self):
        self.save()

    # @classmethod
    # def get_images(cls):
    #     images = cls.objects.all()
    #     return images



class Comments(models.Model):
    comment_content = models.CharField(max_length =85)
    date_posted = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE )
    poster = models.ForeignKey(User,on_delete=models.CASCADE)

    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,date):
        comment = cls.objects.filter(date_posted__date = date)
        return comment

    @classmethod
    def delete_single_comment(cls,comment_id):
        comment = cls.objects.filter(id=comment_id).delete()
        db.session.commit()

    



class Profile(models.Model):
    name = models.CharField(max_length =30)
    bio = models.CharField(max_length =260)
    pic = models.ImageField(upload_to = 'profilepics/', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    contact = models.CharField(max_length =70)
    projez = models.CharField(max_length =70)

    def __str__(self):
        return self.bio

    @classmethod
    def get_profile(cls):
        profile = cls.objects.all()
        return profile

    def save_profile(self):
        self.save()

    def delete_profile(self):
        profile=Profile.objects.all().delete()
        return profile


    def create_profile(sender,**kwargs):
        if kwargs['created']:
            profile=Profile.objects.create(name=kwargs['instance'])
    post_save.connect(create_profile,sender=User)