from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Restaurent(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        OTHER = 'OT', 'Other'

    name = models.CharField(max_length=100)
    website = models.URLField('')
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    restaurent_type = models.CharField(max_length=2, choices=TypeChoices.choices)

    def __str__(self) -> str:
        return self.name

    #Overrinding save method to check if object is created for the first time or not
    # If object created for the first time, it returns TRUE
    # Else it return FALSE    
    def save(self, *args, **kwargs):
        print(self._state.adding)
        if self._state.adding:
            print("You can send me to the respective person - USECASE")
        super().save(*args, **kwargs)
    
    


class Rating(models.Model):
    restaurent = models.ForeignKey(Restaurent, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"Rating: {self.rating}"


class Sales(models.Model):
    restaurent = models.ForeignKey(Restaurent, on_delete=models.SET_NULL, null=True, related_name='sales')
    income = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField()
