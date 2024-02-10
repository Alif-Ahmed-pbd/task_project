from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class Custom_user(AbstractUser):
    USER = [
        ('Admin', 'Admin'),
        ('Usertask', 'Usertask'),
    ]
    username = models.CharField(max_length = 30, null=True )
    email=models.EmailField(unique=True, max_length=100)
    user_type=models.CharField(choices=USER, max_length=50, null=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    def __str__(self):
        return self.username
    

class User_Profile(models.Model):
    first_name=models.CharField(max_length=30, null=True)
    last_name=models.CharField(max_length=30, null=True)
    address=models.CharField(max_length=30, null=True)
    phone=models.CharField(max_length=30, null=True)
    occupation=models.CharField(max_length=30, null=True)
    user=models.OneToOneField(Custom_user, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name+' '+self.last_name
    
class Add_task(models.Model):
    PRIORITY = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    CATEGORIE = [
        ('proggraming', 'proggraming'),
        ('practice', 'practice'),
        ('contest', 'contest'),
    ]
    user = models.ForeignKey(Custom_user, on_delete=models.CASCADE, null=True)
    task_title = models.CharField(max_length=100, null=True)
    task_description = models.TextField()
    task_priority = models.CharField(choices=PRIORITY, max_length=30, null=True)
    due_date = models.DateTimeField(default=timezone.now)
    completion_status = models.BooleanField(default=False)
    task_categorie = models.CharField(choices=CATEGORIE, max_length=30, null=True)


