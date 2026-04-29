from django.db import models


class FuelStation(models.Model):
    truckstop_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, db_index=True)
    state = models.CharField(max_length=50, db_index=True)
    retail_price = models.DecimalField(max_digits=6, decimal_places=3)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["state", "city"]),
            models.Index(fields=["retail_price"]),
        ]
        ordering = ["retail_price"]

    def __str__(self):
        return f"{self.truckstop_name} - {self.city}, {self.state}"