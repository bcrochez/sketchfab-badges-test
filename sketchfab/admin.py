from django.contrib import admin

from .models import SketchfabUser, Model3D, Badge

# Register your models here.

admin.site.register(SketchfabUser)
admin.site.register(Model3D)
admin.site.register(Badge)
