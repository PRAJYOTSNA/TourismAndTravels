from django.contrib import admin
from travelapp.models import State,City,Area,Profile,PlaceMap, Amount, Packages,Booking, Rating

# Register your models here.
admin.site.register(State)
admin.site.register(City)
admin.site.register(Area)
admin.site.register(Profile)
admin.site.register(Amount)
admin.site.register(Packages)
admin.site.register(Booking)
admin.site.register(PlaceMap)
admin.site.register(Rating)

