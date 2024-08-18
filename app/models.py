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
    position = models.PositiveIntegerField()

    class Meta:
        ordering = ["position"]
    
    def __str__(self):
        return f"{self.title}"
    

class Eats(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=300)
    drive_time = models.IntegerField()
    text = models.CharField(max_length=300)
    website = models.CharField(max_length=300, blank=True)
    phone = models.IntegerField()
    position = models.PositiveIntegerField()
    image = models.ImageField(upload_to='eats_pics/', blank=True)

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return f"{self.title}"


class Activity(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=300)
    drive_time = models.IntegerField()
    text = models.CharField(max_length=300)
    website = models.CharField(max_length=300, blank=True)
    position = models.PositiveIntegerField()
    image = models.ImageField(upload_to='eats_pics/', blank=True)

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return f"{self.title}"

