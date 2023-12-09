from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Vaccine)
admin.site.register(Register)
admin.site.register(Schedule)
admin.site.register(Barangay)
admin.site.register(Guardian)