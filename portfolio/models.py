from django.db import models


class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    read_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom}"
