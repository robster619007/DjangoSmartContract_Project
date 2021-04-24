from django.db import models

# Create your models here.
class PostToken(models.Model):
    id = models.AutoField(primary_key = True)
    sender_address = models.CharField(max_length = 150,default = '')
    reciever_address = models.CharField(max_length = 150,default = '')
    value = models.IntegerField(default = 0)
    sender_balances = models.IntegerField(default = 0)
    reciever_balance = models.IntegerField(default = 0)
    private_key = models.CharField(max_length = 150,default = '')

    