from django.contrib import admin

# Register your models here.


from .models import Brand, Beer, TasteOption, ContainerOption

admin.site.register(Brand)
admin.site.register(Beer)
admin.site.register(TasteOption)
admin.site.register(ContainerOption)
