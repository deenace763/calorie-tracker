from django.db import models
from django.contrib.auth.models import User

class CalorieEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    food_name = models.CharField(max_length=255)
    calories = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.food_name} ({self.calories} cal) on {self.date}"
