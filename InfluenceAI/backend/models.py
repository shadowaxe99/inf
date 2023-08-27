```python
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

class Influencer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    social_media_handle = models.CharField(max_length=100)
    followers_count = models.IntegerField()
    engagement_rate = models.FloatField()

class Brand(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)

class Contract(models.Model):
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    contract_terms = models.TextField()
    signed = models.BooleanField(default=False)

class Transaction(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)

class Content(models.Model):
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)
    content_text = models.TextField()
    scheduled_date = models.DateTimeField()
    keywords = models.CharField(max_length=500)
    multimedia = models.FileField(upload_to='uploads/')
```
