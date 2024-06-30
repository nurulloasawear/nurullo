from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from .utils import generate_qr_code, get_youtube_embed_url

class CustomUserManager(UserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    nickname = models.CharField(max_length=255, unique=True, null=True, blank=True)  # Fixed
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    background_image = models.ImageField(upload_to='background_images/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    personal_links = models.URLField(blank=True, null=True)
    personal_links1 = models.URLField(blank=True, null=True)
    personal_links2 = models.URLField(blank=True, null=True)
    background_color = models.CharField(max_length=7, default='#FFFFFF')  # Fixed
    youtube_link = models.URLField(blank=True, null=True)
    qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)  # QR code field
    # Multiple image fields with URLs
    image1 = models.ImageField(upload_to='images/', null=True, blank=True)
    personal1 = models.URLField(blank=True, null=True)
    image2 = models.ImageField(upload_to='images/', null=True, blank=True)
    personal2 = models.URLField(blank=True, null=True)
    image3 = models.ImageField(upload_to='images/', null=True, blank=True)
    personal3 = models.URLField(blank=True, null=True)
    image4 = models.ImageField(upload_to='images/', null=True, blank=True)
    personal4 = models.URLField(blank=True, null=True)
    image5 = models.ImageField(upload_to='images/', null=True, blank=True)
    personal5 = models.URLField(blank=True, null=True)
    image6 = models.ImageField(upload_to='images/', null=True, blank=True)
    personal6 = models.URLField(blank=True, null=True)
    image7 = models.ImageField(upload_to='images/', null=True, blank=True)
    personal7 = models.URLField(blank=True, null=True)
    image8 = models.ImageField(upload_to='images/', null=True, blank=True)
    personal8 = models.URLField(blank=True, null=True)
    image9 = models.ImageField(upload_to='images/', null=True, blank=True)
    personal9 = models.URLField(blank=True, null=True)
    image10 = models.ImageField(upload_to='images/', null=True, blank=True)
    personal10 = models.URLField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.qr_code:
            qr_code_file = generate_qr_code(f'https://yourwebsite.com/profile/{self.nickname}')
            self.qr_code.save(f'{self.nickname}_qr_code.png', qr_code_file, save=False)
        super().save(*args, **kwargs)

    def get_youtube_embed_url(self):
        return get_youtube_embed_url(self.youtube_link)

    def __str__(self):
        return self.email
