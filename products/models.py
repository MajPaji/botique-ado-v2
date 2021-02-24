from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendy_name


class Product(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    has_sizes = models.BooleanField(default=False, blank=True, null=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    image_url = models.URLField(max_length=1024, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)


    def __str__(self):
        return self.name

