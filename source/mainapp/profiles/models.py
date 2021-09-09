from django.db import models

# Django Part 5 Code
# This is a dictionary object that are drop down options in the site admin
PREFIX_CHOICES = {
    ('Ms','Ms'),
    ('Miss','Miss'),
    ('Mrs','Mrs'),
    ('Mr','Mr'),
    ('Dr','Dr'),
}


# Create your models here.
# Django Part 4 Code
class Profile(models.Model):
    prefix = models.CharField(max_length=60, default="", choices=PREFIX_CHOICES) # In part 5 I added this whole line.
    first_name = models.CharField(max_length=60, default="", blank=True, null=False)
    last_name = models.CharField(max_length=60, default="", blank=True, null=False)
    email = models.CharField(max_length=60, default="", blank=True, null=False)
    username = models.CharField(max_length=60, default="", blank=True, null=False)
# Django Part 5 Code
    objects = models.Manager()

    # Returns actual names of product objects that are created in the admin
    def __str__(self):
        return self.first_name