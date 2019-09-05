from django.db import models

# Create your models here.
class Person(models.Model):

    name = models.CharField(max_length = 128)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Person_detail", kwargs={"pk": self.pk})