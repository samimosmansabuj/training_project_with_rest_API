from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
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


@api_view(['POST', 'GET', 'DELETE'])
def social_api_view(request, id=None):
    if id is not None:
        social_link = Social_Link.objects.get(id=id)
    else:
        social_link = Social_Link.objects.all()
    
    if request.method == 'GET':
        if id is not None:
            social_link_serialize = Social_Link_Serializer(social_link)
        else:
            social_link_serialize = Social_Link_Serializer(social_link, many=True)
        return Response(social_link_serialize.data)
    
    if request.method == 'POST':
        data = request.data
        data_serialize = Social_Link_Serializer(data=data)
        if data_serialize.is_valid():
            data_serialize.save()
            msge = "New Added Successfully!"
            return Response(msge)
        else:
            return Response(data_serialize.errors)



class SocialLinkListView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Social_Link.objects.all()
    serializer_class = Social_Link_Serializer

class OfficeAddressListView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Office_Address.objects.all()
    serializer_class = Office_Address_Serializer

class Customer_FeedbackListView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Customer_Feedback.objects.all()
    serializer_class = Customer_Feedback_Serializer

class BlogListView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blog_Serializer

class TechnologyListView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Technology.objects.all()
    serializer_class = Technology_Serializer


