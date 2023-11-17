from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField(null=True)
    parentAge = models.CharField(max_length=40)
    contact = models.IntegerField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"


