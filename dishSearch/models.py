from django.db import models


class Restaurant(models.Model):
        name = models.CharField(max_length=128,null=True)
        items = models.CharField(max_length=25000,null=True)
        location = models.CharField(max_length=256,null=True)
        latitude = models.CharField(max_length=32,null=True)
        longitude = models.CharField(max_length=32,null=True)
        full_details = models.CharField(max_length=3200,null=True)
        cuisines = models.CharField(max_length=512,null=True)
        price_range = models.IntegerField(null=True)
        aggregate_rating = models.FloatField(null=True)
        rating_color = models.CharField(max_length=32,null=True)
        rating_text = models.CharField(max_length=32,null=True)
        votes = models.IntegerField(null=True)
        average_cost_for_two = models.IntegerField(null=True)
        has_online_delivery = models.BooleanField(default = False)
        
        
        def __str__(self) :
              return self.name

    
    