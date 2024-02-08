from django import forms
from core.models import *


class Website_Logo_Form(forms.ModelForm):
    class Meta:
        model = Website_Logo
        fields = ['logo', 'site_title', 'is_active']

class Home_Banner_Form(forms.ModelForm):
    class Meta:
        model = Home_Banner
        fields = ['image', 'title', 'tags', 'is_active']


class Our_Feature_Form(forms.ModelForm):
    class Meta:
        model = Our_Feature
        fields = ['icon', 'title', 'tags', 'description', 'is_active']
    

class Social_Link_Form(forms.ModelForm):
    class Meta:
        model = Social_Link
        fields = ['icon', 'title', 'url_link', 'is_active']

class Office_Address_Form(forms.ModelForm):
    class Meta:
        model = Office_Address
        fields = ['address', 'email', 'phone_number', 'fax_number', 'is_active']

class Customer_Feedback_Form(forms.ModelForm):
    class Meta:
        model = Customer_Feedback
        fields = ['image', 'title', 'tags', 'is_public']

class Blog_Form(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['image', 'title', 'tags', 'description', 'is_active']

class Technology_Form(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ['icon', 'title', 'tags', 'description', 'is_active']

