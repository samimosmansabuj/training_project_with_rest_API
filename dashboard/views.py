from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import *
from core.models import *
import os

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def dashboard_logo(request):
    context = {}
    logos = Website_Logo.objects.all()
    context['logos'] = logos
    
    if request.method == 'POST':
        if request.POST.get('logo_delete'):
            logo_delete = get_object_or_404(Website_Logo, id=request.POST.get('logo_delete'))
            os.remove(logo_delete.logo.path)
            logo_delete.delete()
              
        elif request.POST.get('logo_status'):
            logo_status = get_object_or_404(Website_Logo, id=request.POST.get('logo_status'))
            if logo_status.is_active == True:
                logo_status.is_active = False
            elif logo_status.is_active == False:
                logo_status.is_active = True
            logo_status.save()
        
        return redirect(request.META['HTTP_REFERER'])

    return render(request, 'dashboard/logo/logo.html', context)

def dashboard_logo_add(request, id=None):
    context = {}
    if id:
        logo_object = get_object_or_404(Website_Logo, id=id)
        context['logo'] = logo_object

    if request.method == 'POST':
        logo = request.FILES.get('logo')
        site_title = request.POST.get('site_title')
        status = request.POST.get('status')
        
        if not id:
            logo_object = Website_Logo.objects.create(logo=logo, site_title=site_title)
        else:
            if logo:
                os.remove(logo_object.logo.path)
                logo_object.logo = logo
            logo_object.site_title = site_title
            
        if status:
            logo_object.is_active = True
        else:
            logo_object.is_active = False
        logo_object.save()
        return redirect('dashboard_logo')
        
    
    return render(request, 'dashboard/logo/logo_add.html', context)


def dashboard_banner(request):
    context = {}
    form = Home_Banner_Form()
    context['form'] = form
    banners = Home_Banner.objects.all()
    context['banners'] = banners
    
    if request.method == 'POST':
        if request.POST.get('banner_delete'):
            banner_delete = get_object_or_404(Home_Banner, id=request.POST.get('banner_delete'))
            os.remove(banner_delete.image.path)
            banner_delete.delete()
              
        elif request.POST.get('banner_status'):
            banner_status = get_object_or_404(Home_Banner, id=request.POST.get('banner_status'))
            if banner_status.is_active == True:
                banner_status.is_active = False
            elif banner_status.is_active == False:
                banner_status.is_active = True
            banner_status.save()
        
        return redirect(request.META['HTTP_REFERER'])

    return render(request, 'dashboard/banner.html', context)

def banner_add(request):
    if request.method == 'POST':
        form = Home_Banner_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(request.META['HTTP_REFERER'])
        else:
            return HttpResponse(form.errors)


def dashboard_feature(request):
    context = {}
    features = Our_Feature.objects.all()
    context['features'] = features
    
    if request.method == 'POST':
        if request.POST.get('feature_delete'):
            feature_delete = get_object_or_404(Our_Feature, id=request.POST.get('feature_delete'))
            os.remove(feature_delete.icon.path)
            feature_delete.delete()
              
        elif request.POST.get('feature_status'):
            feature_status = get_object_or_404(Our_Feature, id=request.POST.get('feature_status'))
            print(feature_status.is_active)
            if feature_status.is_active == True:
                feature_status.is_active = False
            elif feature_status.is_active == False:
                feature_status.is_active = True
            feature_status.save()
        
        return redirect(request.META['HTTP_REFERER'])

    return render(request, 'dashboard/feature/feature.html', context)

def feature_add(request, id=None):
    if id:
        feature = get_object_or_404(Our_Feature, id=id)
        form = Our_Feature_Form(instance=feature)
    else:
        form = Our_Feature_Form()
    
    if request.method == 'POST':
        if id:
            form = Our_Feature_Form(request.POST, request.FILES, instance=feature)
        else:
            form = Our_Feature_Form(request.POST, request.FILES)
            
        if form.is_valid():
            form.save()
            return redirect('dashboard_feature')
        else:
            return HttpResponse(form.errors)
    
    return render(request, 'dashboard/feature/feature_add.html', {'form': form})

def dashboard_technology(request):
    context = {}
    technologies = Technology.objects.all()
    context['technologies'] = technologies
    
    if request.method == 'POST':
        if request.POST.get('technology_delete'):
            technology_delete = get_object_or_404(Technology, id=request.POST.get('technology_delete'))
            os.remove(technology_delete.icon.path)
            technology_delete.delete()
              
        elif request.POST.get('technology_status'):
            technology_status = get_object_or_404(Technology, id=request.POST.get('technology_status'))
            if technology_status.is_active == True:
                technology_status.is_active = False
            elif technology_status.is_active == False:
                technology_status.is_active = True
            technology_status.save()
        
        return redirect(request.META['HTTP_REFERER'])

    return render(request, 'dashboard/technology/technology.html', context)

def technology_add(request, id=None):
    if id:
        technology = get_object_or_404(Technology, id=id)
        form = Technology_Form(instance=technology)
    else:
        form = Technology_Form()
    
    if request.method == 'POST':
        if id:
            form = Technology_Form(request.POST, request.FILES, instance=technology)
        else:
            form = Technology_Form(request.POST, request.FILES)
            
        if form.is_valid():
            form.save()
            return redirect('dashboard_technology')
        else:
            return HttpResponse(form.errors)
    
    return render(request, 'dashboard/technology/technology_add.html', {'form': form})




def dashboard_blog(request):
    context = {}
    blogs = Blog.objects.all()
    context['blogs'] = blogs
    
    if request.method == 'POST':
        if request.POST.get('blog_delete'):
            blog_delete = get_object_or_404(Blog, id=request.POST.get('blog_delete'))
            os.remove(blog_delete.image.path)
            blog_delete.delete()
              
        elif request.POST.get('blog_status'):
            blog_status = get_object_or_404(Blog, id=request.POST.get('blog_status'))
            if blog_status.is_active == True:
                blog_status.is_active = False
            elif blog_status.is_active == False:
                blog_status.is_active = True
            blog_status.save()
        
        return redirect(request.META['HTTP_REFERER'])

    return render(request, 'dashboard/blog/blog.html', context)


def blog_add(request, id=None):
    if id:
        blog = get_object_or_404(Blog, id=id)
        form = Blog_Form(instance=blog)
    else:
        form = Blog_Form()
    
    if request.method == 'POST':
        if id:
            form = Blog_Form(request.POST, request.FILES, instance=blog)
        else:
            form = Blog_Form(request.POST, request.FILES)
            
        if form.is_valid():
            if id:
                blog.image.delete()
            form.save()
            return redirect('dashboard_blog')
        else:
            return HttpResponse(form.errors)
    
    return render(request, 'dashboard/blog/blog_add.html', {'form': form})




