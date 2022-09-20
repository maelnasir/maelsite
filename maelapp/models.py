from django.db import models
from datetime import date

class Portfolio(models.Model):
    project = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    startDate = models.DateField(("Project Start Date"), default=date.today)
    endDate = models.DateField(("Project End Date"), default=date.today)
    description = models.CharField(max_length=500)
    # adjust model name
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Previous Projects"

class Feedback(models.Model):
    # add fields
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    feedback = models.CharField(max_length=500)
    
    # adjust model name
    class Meta:
        verbose_name = "Response"
        verbose_name_plural = "Responses"

class UploadImage(models.Model):  
    caption = models.CharField(max_length=200)  
    image = models.ImageField(upload_to='images')  

    class Meta:
        verbose_name = "Front Image"
        verbose_name_plural = "Front Image"
  
    def __str__(self):  
        return self.caption  