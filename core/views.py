from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .models import *
from .serializers import *

# Create your views here.
def index(request):
    banner = Home_Banner.objects.filter(is_active=True).first()
    featuers = Our_Feature.objects.filter(is_active=True)[:3]
    technologies = Technology.objects.filter(is_active=True)[:4]
    technologies_icons = Technology_Icon.objects.all()
    blogs = Blog.objects.filter(is_active=True)
    customer_feedbacks = Customer_Feedback.objects.filter(is_public=True)
    templates = Templates.objects.filter(is_active=True)
    map_images = Map_Image.objects.filter(is_active=True).first()
    office_address = Office_Address.objects.filter(is_active=True)[:2]
    social_links = Social_Link.objects.filter(is_active=True)
    
    context = {
        'banner': banner,
        'featuers': featuers,
        'technologies': technologies,
        'technologies_icons': technologies_icons,
        'blogs': blogs,
        'customer_feedbacks': customer_feedbacks,
        'templates': templates,
        'map_images': map_images,
        'office_address': office_address,
        'social_links': social_links,
    }
    
    return render(request, 'index.html', context)


def Login(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
    return render(request, 'login.html', {'form': form})

def Logout(request):
    logout(request)
    return redirect('login')






class SocialLinkListView(ListCreateAPIView):
    queryset = Social_Link.objects.all()
    serializer_class = Social_Link_Serializer

class OfficeAddressListView(ListCreateAPIView):
    queryset = Office_Address.objects.all()
    serializer_class = Office_Address_Serializer

class Customer_FeedbackListView(ListCreateAPIView):
    queryset = Customer_Feedback.objects.all()
    serializer_class = Customer_Feedback_Serializer

class BlogListView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blog_Serializer

class TechnologyListView(ListCreateAPIView):
    queryset = Technology.objects.all()
    serializer_class = Technology_Serializer


