from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    type = models.CharField(max_length=50)       # Tablet, Syrup, Injection
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField()
    uses = models.TextField()
    side_effects = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name
