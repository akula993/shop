from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_category')
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    SIZE_CLASS = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('EL', 'Extra Large'),

    )
    name = models.CharField(max_length=255)
    uuid = models.UUIDField()
    description = models.TextField
    price = models.DecimalField(max_digits=10, decimal_places=2, )
    size = models.CharField(max_length=1, choices=SIZE_CLASS, default='Small')
    lot = models.IntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    creation_up = models.DateTimeField(auto_now=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='brand')
    # rating = models.
