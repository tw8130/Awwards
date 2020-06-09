from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Review,Project
from django.forms import ModelForm, Textarea, IntegerField

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Email Address")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user',]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [ 'usability_rating', 'design_rating', 'content_rating' , 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15}),
        }
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class VoteForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('design','usability','content')