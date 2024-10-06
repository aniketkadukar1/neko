from django.contrib.auth.models import User
from core.models import Restaurent, Rating, Sales
from django.db import connection
from pprint import pprint

def run():
    chinese = Restaurent.TypeChoices.CHINESE
    restaurent = Restaurent.objects.filter(restaurent_type = chinese, name__startswith='C')
    pprint(restaurent)