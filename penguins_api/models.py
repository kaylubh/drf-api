from django.db import models
from django.contrib.auth import get_user_model


class Penguin(models.Model):
    # fields
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_add=True)

    def __str__(self):
        return self.name
