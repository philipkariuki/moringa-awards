from django.test import TestCase
from .models import Project, Profile, Comments

class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.projo= Project(title = 'zproject Mpya', description ='Hii ni description ya test project', link= 'https;//www.testproject.co.ug',  projimage='articles/project.png')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.projo,Project))

    # Testing Save Method
    def test_save_method(self):
        self.projo.save_project()
        
            
    # Testing new project
    def test_new_project(self):
        self.new_project= Project(title = 'Test Project',description = 'This is a random test project description', link= 'https;//www.testproject.co.ug',  projimage='articles/project.png')
        self.new_project.save()
        
    def tearDown(self):
        Project.objects.all().delete()
  

class ProfileTestClass(TestCase):
         
    def setUp(self):
        self.pablo = Profile(name='pablo', bio='hii ni bio')

    def test_instance(self):
        self.assertTrue(isinstance(self.pablo, Profile))
        
    
    def tearDown(self):
        Profile.objects.all().delete()
        
    

class CommentsTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.projo= Comments( comment_content = 'Wow! Nice project!' )
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.projo,Comments))
        
    # Testing Save Method
    def test_save_method(self):
        self.projo.save_comments()

