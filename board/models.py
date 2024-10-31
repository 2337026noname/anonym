from django.db import models

# Create your models here.

class Put (models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    count = models.IntegerField(default=0)
    writer = models.CharField(max_length=30, default='anonymous')
    passwd = models.CharField(max_length=30)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.title