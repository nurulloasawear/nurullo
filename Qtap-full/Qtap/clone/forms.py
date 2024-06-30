from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('nickname', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['nickname'].required = True

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'profile_image', 'description', 'personal_links', 'personal_links1',
            'personal_links2', 'background_color', 'background_image',
            'image1', 'personal1', 'image2', 'personal2',
            'image3', 'personal3', 'image4', 'personal4',
            'image5', 'personal5', 'image6', 'personal6',
            'image7', 'personal7', 'image8', 'personal8',
            'image9', 'personal9', 'image10', 'personal10', 'youtube_link'
        ]

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        # O'chirib tashlandi, chunki email maydoni formda mavjud emas
        # self.fields['email'].required = True

