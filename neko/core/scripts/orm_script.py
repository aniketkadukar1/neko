from django.contrib.auth.models import User
from core.models import Restaurent, Rating, Sales
from django.db import connection
from pprint import pprint

def run():
    restaurent = Restaurent.objects.select_related()
    pprint(restaurent)
    print("_________________________________________________")
    

    print("_________________________________________________")
    
    pprint(connection.queries)