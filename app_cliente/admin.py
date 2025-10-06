from django.contrib import admin

# Register your models here.

from .models import Cliente
# Registrar el modelo Cliente en el admin
admin.site.register(Cliente)
