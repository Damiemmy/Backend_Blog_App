from django.db import models
from django.conf import settings
import uuid
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

# Create your models here.

User=get_user_model()
class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)
    image=models.ImageField(upload_to='img',blank=True,null=True)
    bio=models.TextField(max_length=400,blank=True,null=True)
    state=models.CharField(max_length=100,blank=True,null=True)
    city=models.CharField(max_length=100,blank=True,null=True)
    email=models.CharField(max_length=100,blank=True,null=True)
    country=models.CharField(max_length=100,blank=True,null=True)
    phone=models.CharField(max_length=100,blank=True,null=True)
    verified=models.BooleanField(default=False)
    address=models.TextField(max_length=100,blank=True,null=True)

    def __str__(self):
        return f"{self.user}'s Profile"

def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance,state=instance.state,address=instance.address,email=instance.email,phone=instance.phone,city=instance.city)

def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()

post_save.connect(create_user_profile,sender=User)
post_save.connect(save_user_profile,sender=User)

class Blogs(models.Model):
    category=(
        ('GOVERNMENT','GOVERNMENT'),
        ('ECONONMY','ECONOMY'),
        ('TECHNOLOGY','TECHNOLOGY'),
        ('EDUCATION','EDUCATION'),
        ('FARMING','FARMING'),
    )
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=150)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True, null=True)
    description=models.TextField(max_length=3000)
    slug=models.SlugField(blank=True,null=True)
    image=models.ImageField(upload_to='blog-image',blank=True,null=True)
    category=models.CharField(max_length=100,choices=category,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            Base_slug=slugify(self.title)
            slug=Base_slug
            counter=1
            while Blogs.objects.filter(slug=slug).exists():
                slug=f"{Base_slug}-{counter}"
                counter=counter+1
            self.slug=slug
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title