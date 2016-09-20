from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Query(models.Model):
    ques = models.CharField(max_length=100, null=True)
    # property=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.ques
