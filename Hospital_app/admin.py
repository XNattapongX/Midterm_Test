from django.contrib import admin
from .models import * #เอามาหมดทุก Class

# Register your models here.
admin.site.register(d_type)
admin.site.register(product)
admin.site.register(userbuy)
admin.site.register(report_buy)
