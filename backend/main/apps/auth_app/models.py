from django.db import models


class Record(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    username = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"User regitered: {self.name}, {self.username}, {self.password}"
