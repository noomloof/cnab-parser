from django.db import models
import uuid

class Business(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    owner_name = models.CharField(max_length=90)
    business_name = models.CharField(max_length=200)