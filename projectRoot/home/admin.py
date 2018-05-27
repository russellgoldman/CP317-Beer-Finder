from django.contrib import admin

# Register your models here.


from .models import Brand, Beer, Taste, BodyType, ContainerStyle

admin.site.register(Brand)
admin.site.register(Beer)
admin.site.register(Taste)
admin.site.register(BodyType)
admin.site.register(ContainerStyle)
