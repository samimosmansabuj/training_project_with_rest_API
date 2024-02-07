from django.db import models

class Website_Logo(models.Model):
    logo = models.ImageField(upload_to='logo/')
    site_title = models.CharField(max_length=500, blank=True, null=True)
    
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.logo.name


class Home_Banner(models.Model):
    image = models.ImageField(upload_to='banner/')
    title = models.CharField(max_length=500)
    tags = models.TextField(max_length=500, blank=True, null=True)
    
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.image.name


class Our_Feature(models.Model):
    icon = models.ImageField(upload_to='feature_icon/', blank=True, null=True)
    title = models.CharField(max_length=500)
    tags = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    is_active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title


class Technology(models.Model):
    icon = models.ImageField(upload_to='technology/', blank=True, null=True)
    title = models.CharField(max_length=500)
    tags = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    is_active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title

class Technology_Icon(models.Model):
    technology = models.OneToOneField(Technology, on_delete=models.CASCADE, blank=True, null=True)
    icon = models.ImageField(upload_to='technology_icon/')
    
    def __str__(self) -> str:
        return self.icon.name

class Blog(models.Model):
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    title = models.CharField(max_length=500)
    tags = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    is_active = models.BooleanField(default=False)
    
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title


class Customer_Feedback(models.Model):
    image = models.ImageField(upload_to='customer_feedback/', blank=True, null=True)
    title = models.CharField(max_length=500)
    tags = models.TextField(blank=True, null=True)
    
    is_public = models.BooleanField(default=False)
    
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title

class Templates(models.Model):
    image = models.ImageField(upload_to='templates/', blank=True, null=True)
    title = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    preview_url = models.URLField(max_length=800)
    
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title

class Map_Image(models.Model):
    image = models.ImageField(upload_to='map/', blank=True, null=True)
    
    is_active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.image.name


class Office_Address(models.Model):
    address = models.CharField(max_length=700)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=14)
    fax_number = models.CharField(max_length=14)
    
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.address


class Social_Link(models.Model):
    SOCIAL_MEDIA = (
        ('Facebook', 'Facebook'),
        ('Twitter', 'Twitter'),
        ('Linkedin', 'Linkedin'),
        ('Instagram', 'Instagram'),
        ('Youtube', 'Youtube'),
    )
    icon = models.ImageField(upload_to='social_icon/')
    title = models.CharField(max_length=100, choices=SOCIAL_MEDIA)
    url_link = models.URLField(max_length=500, blank=True, null=True)
    
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title
