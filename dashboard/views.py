from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import *
from core.models import *
from django.contrib.auth.decorators import login_required
import os

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
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

@login_required
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


@login_required
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

@login_required
def banner_add(request):
    if request.method == 'POST':
        form = Home_Banner_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(request.META['HTTP_REFERER'])
        else:
            return HttpResponse(form.errors)

@login_required
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

@login_required
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


@login_required
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

@login_required
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


@login_required
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

@login_required
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
            form.save()
            return redirect('dashboard_blog')
        else:
            return HttpResponse(form.errors)
    
    return render(request, 'dashboard/blog/blog_add.html', {'form': form})


@login_required
def dashboard_customer_feedback(request):
    context = {}
    customer_feedback = Customer_Feedback.objects.all()
    context['customer_feedback'] = customer_feedback
    
    if request.method == 'POST':
        if request.POST.get('customer_feedback_delete'):
            customer_feedback_delete = get_object_or_404(Customer_Feedback, id=request.POST.get('customer_feedback_delete'))
            os.remove(customer_feedback_delete.image.path)
            customer_feedback_delete.delete()
              
        elif request.POST.get('customer_feedback_status'):
            customer_feedback_status = get_object_or_404(Customer_Feedback, id=request.POST.get('customer_feedback_status'))
            if customer_feedback_status.is_public == True:
                customer_feedback_status.is_public = False
            elif customer_feedback_status.is_public == False:
                customer_feedback_status.is_public = True
            customer_feedback_status.save()
        
        return redirect(request.META['HTTP_REFERER'])

    return render(request, 'dashboard/feedback/customer_feedback.html', context)

@login_required
def customer_feedback_add(request, id):
    customer_feedback = get_object_or_404(Customer_Feedback, id=id)
    form = Customer_Feedback_Form(instance=customer_feedback)
    
    if request.method == 'POST':
        form = Customer_Feedback_Form(request.POST, request.FILES, instance=customer_feedback)  
        if form.is_valid():
            # previous_image_path = customer_feedback.image.path
            # if customer_feedback.image:
            #     os.remove(previous_image_path)
            #     customer_feedback.image.delete()
            # print(form)
            form.save()
            return redirect('dashboard_customer_feedback')
        else:
            return HttpResponse(form.errors)
    
    return render(request, 'dashboard/feedback/update_customer_feedback.html', {'form': form})


@login_required
def dashboard_map(request):
    context = {}
    maps = Map_Image.objects.all()
    context['maps'] = maps
    
    if request.method == 'POST':
        if request.POST.get('map_delete'):
            map_delete = get_object_or_404(Map_Image, id=request.POST.get('map_delete'))
            os.remove(map_delete.image.path)
            map_delete.delete()
              
        elif request.POST.get('map_status'):
            map_status = get_object_or_404(Map_Image, id=request.POST.get('map_status'))
            if map_status.is_active == True:
                map_status.is_active = False
            elif map_status.is_active == False:
                map_status.is_active = True
            map_status.save()
        
        return redirect(request.META['HTTP_REFERER'])

    return render(request, 'dashboard/map/dashboard_map.html', context)

@login_required
def add_map(request, id=None):
    context = {}
    if id:
        map_object = get_object_or_404(Map_Image, id=id)
        context['map_object'] = map_object

    if request.method == 'POST':
        map_image = request.FILES.get('map_image')
        status = request.POST.get('status')
        
        if not id:
            map_object = Map_Image.objects.create(image=map_image)
        else:
            if map_image:
                os.remove(map_object.image.path)
                map_object.image = map_image
            
        if status:
            map_object.is_active = True
        else:
            map_object.is_active = False
        map_object.save()
        return redirect('dashboard_map')
        
    return render(request, 'dashboard/map/add_map.html', context)


@login_required
def dashboard_office_address(request):
    context = {}
    office_address = Office_Address.objects.all()
    context['office_address'] = office_address
    
    if request.method == 'POST':
        if request.POST.get('office_address_delete'):
            office_address_delete = get_object_or_404(Office_Address, id=request.POST.get('office_address_delete'))
            office_address_delete.delete()
              
        elif request.POST.get('office_address_status'):
            office_address_status = get_object_or_404(Office_Address, id=request.POST.get('office_address_status'))
            if office_address_status.is_active == True:
                office_address_status.is_active = False
            elif office_address_status.is_active == False:
                office_address_status.is_active = True
            office_address_status.save()
        
        return redirect(request.META['HTTP_REFERER'])

    return render(request, 'dashboard/office_address/office_address.html', context)

@login_required
def add_office_address(request, id=None):
    if id:
        office_address = get_object_or_404(Office_Address, id=id)
        form = Office_Address_Form(instance=office_address)
    else:
        form = Office_Address_Form()
    
    if request.method == 'POST':
        if id:
            form = Office_Address_Form(request.POST, instance=office_address)  
        else:
            form = Office_Address_Form(request.POST)
            
        if form.is_valid():
            form.save()
            return redirect('dashboard_office_address')
        else:
            return HttpResponse(form.errors)
    
    return render(request, 'dashboard/office_address/add_office_address.html', {'form': form})


@login_required
def dashboard_social_link(request):
    context = {}
    social_links = Social_Link.objects.all()
    context['social_links'] = social_links
    
    if request.method == 'POST':
        if request.POST.get('social_link_delete'):
            social_link_delete = get_object_or_404(Social_Link, id=request.POST.get('social_link_delete'))
            social_link_delete.delete()
              
        elif request.POST.get('social_link_status'):
            social_link_status = get_object_or_404(Social_Link, id=request.POST.get('social_link_status'))
            if social_link_status.is_active == True:
                social_link_status.is_active = False
            elif social_link_status.is_active == False:
                social_link_status.is_active = True
            social_link_status.save()
        
        return redirect(request.META['HTTP_REFERER'])

    return render(request, 'dashboard/social_link/social_link.html', context)

@login_required
def add_social_link(request, id=None):
    if id:
        social_link = get_object_or_404(Social_Link, id=id)
        form = Social_Link_Form(instance=social_link)
    else:
        form = Social_Link_Form()
    
    if request.method == 'POST':
        if id:
            form = Social_Link_Form(request.POST, request.FILES, instance=social_link)  
        else:
            form = Social_Link_Form(request.POST, request.FILES,)
            
        if form.is_valid():
            form.save()
            return redirect('dashboard_social_link')
        else:
            return HttpResponse(form.errors)
    
    return render(request, 'dashboard/social_link/add_social_link.html', {'form': form})




