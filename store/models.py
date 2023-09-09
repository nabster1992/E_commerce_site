from django.contrib.auth.models import User
from django.db import models

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #below allws to to have most recent dress listed first
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_display_price(self):
        return self.price




