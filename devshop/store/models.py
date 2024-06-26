from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
   title = models.CharField(max_length=50)
   slug = models.SlugField(max_length=50)

   class Meta:
      verbose_name_plural = 'Categories'

   def __str__(self):
      return self.title


class Product(models.Model):
   DRAFT = 'draft'
   WAITING_APPROVAL = 'watingapproval'
   ACTIVE = 'active'
   DELETED = 'deleted'

   STATUS_CHOICES = (
      (DRAFT, 'Draft'),
      (WAITING_APPROVAL, 'Wating approval'),
      (ACTIVE, 'Active'),
      (DELETED, 'Deleted')
   )

   user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
   category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
   title = models.CharField(max_length=100)
   slug = models.SlugField(max_length=100)
   description = models.TextField(blank=True)
   price = models.IntegerField()
   image = models.ImageField(upload_to='uploads/product_images/', blank=True, null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)

   class Meta:
      ordering = ["-created_at"]

   def __str__(self) -> str:
      return self.title