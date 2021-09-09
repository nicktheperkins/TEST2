from django.db import models

# Django Part 5 Code
# This is a dictionary object that are drop down options in the site admin
TYPE_CHOICES = {
    ('appetizers','appetizers'),
    ('entrees','entrees'),
    ('treats','treats'),
    ('drinks','drinks'),
}


# Create your models here.
# Django Part 4 Code
class Product(models.Model):
    type = models.CharField(max_length=60, choices=TYPE_CHOICES) # In part 5 I added choices=TYPE_CHOICES
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    description = models.TextField(max_length=300, default="", blank=True)
    price = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)
    image = models.CharField(max_length=255, default='', blank=True)
# Django Part 5 Code
    objects = models.Manager()
    # Returns actual names of product objects that are created in the admin
    def __str__(self):
        return self.name