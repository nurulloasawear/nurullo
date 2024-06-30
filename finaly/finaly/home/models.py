from django.db import models

# Create your models here.
class Treners(models.Model):
    TRENER = 'trener'
    DIRECTOR = 'director'
    USER = 'user'
    MANAGER = 'manager'

    ROLE_CHOICES = (
        (TRENER, 'Trener'),
        (DIRECTOR, 'Director'),
        (USER, 'User'),
        (MANAGER, 'Manager'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    staff = models.CharField(choices=ROLE_CHOICES, max_length=20)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def imageURL(self):
        return self.image.url
    
    
    def __str__(self):
        return self.name
    
class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.name