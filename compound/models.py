from django.db import models

class Simulation(models.Model):
    principal = models.FloatField()
    rate = models.FloatField()
    years = models.FloatField()
    frequency = models.IntegerField()
    final_amount = models.FloatField()
    interests = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Simulation {self.id} - Capital: {self.principal}€"