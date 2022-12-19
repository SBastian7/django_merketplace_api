import uuid, random, string
from django.db import models
from utils.BaseModel import BaseModel

# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=20, blank=False, null=False)  

    def __str__(self):
        return "Category | {}".format(self.name)

class Product(BaseModel):
    SKU = models.CharField(max_length=50, default=''.join(random.choices(string.ascii_uppercase + string.digits, k=7)), editable=False)
    name = models.CharField(max_length=30, null=False, blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=0, null=False, blank=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    image_field = models.ImageField(upload_to='products', null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField(blank=False, null=False)

    def __str__(self) -> str:
        return "Product | {} - {}".format(self.SKU, self.name)

# class ListImages(BaseModel):
#     mainimage = models.ImageField(upload_to='products', null = True)
#     image = models.ForeignKey(Product, on_delete=models.CASCADE)
