from django.contrib import admin
from polls.models import registar_cliente
from polls.models import registrar_gastos

# Register your models here.

admin.site.register(registar_cliente)

admin.site.register(registrar_gastos)