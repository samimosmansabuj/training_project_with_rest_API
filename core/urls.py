from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    
    
    path('api/social-link/', SocialLinkListView.as_view(), name='SocialLinkListView'),
    path('api/office-address/', OfficeAddressListView.as_view(), name='OfficeAddressListView'),
    path('api/customer-feedback/', Customer_FeedbackListView.as_view(), name='Customer_FeedbackListView'),
    path('api/blog/', BlogListView.as_view(), name='LogoUpdateView'),
    path('api/technology/', TechnologyListView.as_view(), name='TechnologyListView'),
]