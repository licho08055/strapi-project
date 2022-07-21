from django.contrib import admin


from .models import Planet, Character, People

admin.site.register(Planet)
admin.site.register(Character)
admin.site.register(People)
