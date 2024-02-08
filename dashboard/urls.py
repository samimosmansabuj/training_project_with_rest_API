from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('logo/', dashboard_logo, name='dashboard_logo'),
    path('logo-add/', dashboard_logo_add, name='dashboard_logo_add'),
    path('logo-update/<int:id>/', dashboard_logo_add, name='update_logo'),
    
    path('banner/', dashboard_banner, name='dashboard_banner'),
    path('banner/add/', banner_add, name='banner_add'),
    
    
    
    path('feature/', dashboard_feature, name='dashboard_feature'),
    path('feature-add/', feature_add, name='feature_add'),
    path('feature-update/<int:id>/', feature_add, name='feature_update'),
    
    
    path('technology/', dashboard_technology, name='dashboard_technology'),
    path('technology-add/', technology_add, name='technology_add'),
    path('technology-update/<int:id>/', technology_add, name='technology_update'),
    
    
    path('blog/', dashboard_blog, name='dashboard_blog'),
    path('blog-add/', blog_add, name='blog_add'),
    path('blog-update/<int:id>/', blog_add, name='blog_update'),
    
    
]