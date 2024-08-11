from django.db import models

# Create your models here.
class Rule(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=300)
    subtext = models.CharField(max_length=300, blank=True)
    position = models.PositiveIntegerField()

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return f"#{self.position}: {self.text}"

class Information(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=300)
    subtext = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='info_pics/', blank=True)
    
    def __str__(self):
        return f"{self.title}"
    