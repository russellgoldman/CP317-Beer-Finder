from django.contrib import admin

# Register your models here.


from .models import Brand, BodyType, Colour, ContainerType, Taste, Beer, Rating

admin.site.register(Brand)
admin.site.register(BodyType)
admin.site.register(Colour)

admin.site.register(ContainerType)
admin.site.register(Taste)

admin.site.register(Beer)

admin.site.register(Rating)
