from django import forms
from rango.models import Page, Category, UserProfile
from django.contrib.auth.models import User


# codes can also be put in models.py
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    # the fields are hidden. Users cannot enter a value for these fields
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # link ModelForm with model
        model = Page
        # fields that are included in the form
        # foreign key hidden
        exclude = ('category',)
        # can also include by: 
        # fields = ('title', 'url', 'views')
    
    # the clean() method
    def clean(self):
        cleaned_data = self.cleaned_data
        # get method provided by the dictionary object. get() returns None if a user doens't enter a value into a form field
        url = cleaned_data.get('url')

        # this doesn't deal with the situation of 'https://'
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        
        return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)