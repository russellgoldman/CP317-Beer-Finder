from django.contrib import admin

# Register your models here.


from .models import Brand, BodyType, Beer, Taste, ContainerType, Rating, Colour

admin.site.register(Brand)
admin.site.register(BodyType)
admin.site.register(Beer)
admin.site.register(Taste)
admin.site.register(ContainerType)
admin.site.register(Rating)
admin.site.register(Colour)
