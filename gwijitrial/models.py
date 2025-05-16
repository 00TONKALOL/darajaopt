from django.db import models


class Transaction(models.Model):
    ID = models.AutoField(primary_key=True)


phone = models.CharField(max_length=20)
amount = models.IntegerField(max_length=20)
merchant_id = models.CharField(max_length=100)
check_id = models.CharField(max_length=100)
status = models.BooleanField(default=False)
created_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
