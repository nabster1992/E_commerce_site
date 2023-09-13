from django.contrib.auth.models import User
from django.db import models
from django.core.files import File
from io import BytesIO
from PIL import Image

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Product(models.Model):
    DRAFT = 'draft'
    AWAITING_APPROVAL = 'Waiting approval'
    ACTIVE = 'active'
    DELETED = 'deleted'

    STATUS_CHOICES = ((DRAFT, 'Draft'),
                      (AWAITING_APPROVAL,'Awaiting approval'),
                      (ACTIVE, 'Active'),
                      (DELETED, 'Deleted')
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)
    #this is so that if you delete the category all products will also be deleted
    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    # 2 attributes sharing same related_name is a problem, changing it would impact other code and id have to fix it
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploads/product_images/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/product_images/thumbnail', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #below allws to to have most recent dress listed first
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_display_price(self):
        return self.price
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                 self.thumbnail = self.make_thumbnail (self.image)
                 self.save()
            
                 return self.thumbnail.url 
            else:
                return 'https://placehold.co/240x240'

    
    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'PNG', quality=85)
        name = image.name.replace('uploads/product_images', '')
        thumbnail = File(thumb_io, name=name)

        return thumbnail
    
class Order(models.Model):
    created_by = models.ForeignKey(User, related_name= 'orders', on_delete=models.PROTECT, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    total_cost = models.IntegerField(default=0)
    paid_amount = models.IntegerField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    payment_intent = models.CharField(max_length=255)

class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def get_display_price(self):
        return self.price / 100







