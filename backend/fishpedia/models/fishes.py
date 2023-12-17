from django.db import models

class Fish(models.Model):
    name = models.CharField(max_length=100)
    min_population = models.IntegerField(null=True, blank=True, verbose_name="Minimal amount")
    max_population = models.IntegerField(null=True, blank=True, verbose_name="Maximal amount")
    tank_size_liters = models.IntegerField(verbose_name="Minimal tank size (liters)")

    def __str__(self):
        return self.name
