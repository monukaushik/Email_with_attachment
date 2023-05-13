from django.db import models


class emailsend(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
   

    def __str__(self):
        return self.username + self.useremail