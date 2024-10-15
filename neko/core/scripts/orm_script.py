from django.contrib.auth.models import User
from core.models import Restaurent, Rating, Sales
from django.db import connection
from pprint import pprint
from django.db.models import F

def run():
    rating = Rating.objects.filter(rating=3).first()
    rating.rating = F('rating') + 1
    rating.save()
    rating.refresh_from_db()
    print(rating.rating)