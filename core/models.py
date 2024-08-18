from django.contrib.auth import get_user_model
from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(
        max_length=255,
    )
    description = models.TextField(
        max_length=1000,
    )
    sort = models.PositiveSmallIntegerField(
        default=0
    )
    active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ('-sort',)

    def __str__(self):
        return self.title


class Product(BaseModel):
    class Colors:
        RED = '#ff0000'
        BLACK = '#000000'
        WHITE = '#ffffff'
        GREEN = '#00ff00'
        BLUE = '#0000ff'

    COLORS = (
        (Colors.RED, 'Red'),
        (Colors.GREEN, 'Green'),
        (Colors.BLUE, 'Blue'),
        (Colors.BLACK, 'Black'),
        (Colors.WHITE, 'White'),
    )

    title = models.CharField(
        max_length=255,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    color = models.CharField(
        max_length=7,
        choices=COLORS,
    )
    active = models.BooleanField(
        default=True
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
    )

    def __str__(self):
        return self.title


class Review(BaseModel):
    body = models.TextField(
        max_length=3000,
    )
    rate = models.PositiveSmallIntegerField()
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
