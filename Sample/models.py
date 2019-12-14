from django.db import models

class Assignment(models.Model):
    filefield = models.FileField(editable=True,null=False)
    charfield = models.CharField(max_length=50, editable=True,null = False)

def __str__(self):
    return self.charfield