from rest_framework import serializers
from rest_framework.views import APIView
from .models import *

class Social_Link_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Social_Link
        fields = ['icon', 'title', 'url_link', 'is_active']

class Office_Address_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Office_Address
        fields = ['address', 'email', 'phone_number', 'fax_number', 'is_active']

class Customer_Feedback_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Feedback
        fields = ['image', 'title', 'tags', 'is_public']

class Blog_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['image', 'title', 'tags', 'description', 'is_active']

class Technology_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['icon', 'title', 'tags', 'description', 'is_active']





