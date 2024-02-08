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
    
    path('feedback/', dashboard_customer_feedback, name='dashboard_customer_feedback'),
    path('customer-feedback-update/<int:id>/', customer_feedback_add, name='customer_feedback_add'),
    
    
    path('map/', dashboard_map, name='dashboard_map'),
    path('map-add/', add_map, name='add_map'),
    path('map-update/<int:id>/', add_map, name='update_map'),
    
    path('office-address/', dashboard_office_address, name='dashboard_office_address'),
    path('office-address-add/', add_office_address, name='add_office_address'),
    path('office-address-update/<int:id>/', add_office_address, name='update_office_address'),
    
    path('social-link/', dashboard_social_link, name='dashboard_social_link'),
    path('social-link-add/', add_social_link, name='add_social_link'),
    path('social-link-update/<int:id>/', add_social_link, name='update_social_link'),
    
    
]