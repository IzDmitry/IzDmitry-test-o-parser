from django.db import models


class Product(models.Model):
    name: str = models.TextField(null=True, blank=True)
    price: int = models.IntegerField(null=True, blank=True)
    description: str = models.TextField(null=True, blank=True)
    image_url: str = models.TextField(null=True, blank=True)
    discount: str = models.CharField(max_length=50, null=True, blank=True)
    url: str = models.TextField(null=True, blank=True)
    date: str = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
