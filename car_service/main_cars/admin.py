from django.contrib import admin
from . import models
from django.utils.translation import gettext_lazy as _

class CarAdmin(admin.ModelAdmin):
    list_display = ('license_plate','model_make','customer','vin_code', 'client')
    search_fields = ('customer', 'client' )

class ModelMakeAdmin(admin.ModelAdmin):
    list_display = ('model', 'make')

class OrderLinesInline(admin.TabularInline):
    model = models.OrderLine
    can_delete = True
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('car', 'date', 'formatted_order_total', 'status')
    search_fields = ('car__customer', 'car__license_plate')
    ordering = ('-date',)
    inlines = (OrderLinesInline, )

    def formatted_order_total(self, obj):
        return f'${obj.order_total}'
    formatted_order_total.short_description = 'Order Total'
    
    def car_details(self, obj):
        return f"{obj.car.customer} - {obj.car.license_plate} - {obj.car.model_make}"

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name','price')

class OrderCommentAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'client', 'comment')
    list_display_links = ('created_at', )

admin.site.register(models.ModelMake, ModelMakeAdmin)
admin.site.register(models.Car, CarAdmin)
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderLine)
admin.site.register(models.OrderComment, OrderCommentAdmin)

