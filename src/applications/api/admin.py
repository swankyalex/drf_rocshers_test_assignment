from django.contrib import admin

from .models import Pointer
from .models import Station

admin.site.register(Station)
admin.site.register(Pointer)
