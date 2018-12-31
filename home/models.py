from django.db import models
# Create your models here.

    

class HomeCategorie(models.Model):
    home_categorie_type = models.CharField(max_length=15, blank=False, null=False)
    name= models.CharField(max_length=40, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
   
    def __str__(self):
        return self.name
        
        
class homeImage(models.Model):
    home_image = models.ImageField(upload_to="home_images" , null=True, blank=True)
   

    def __str__(self):
        return self.home.name