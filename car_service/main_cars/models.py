from django.db import models
from django.utils.translation import gettext_lazy as _

class ModelMake(models.Model):
    model = models.CharField(_('model'), max_length=255)
    make = models.CharField(_('make'),max_length=255)

    def __str__(self) -> str:
        return f'{self.model} {self.make}'

class Car(models.Model):
    customer = models.CharField(_('customer'),max_length=255)
    license_plate = models.CharField(_('license plate'),max_length=10)
    vin_code = models.CharField(_('VIN code'),max_length=17)
    model_make = models.ForeignKey(ModelMake, on_delete=models.CASCADE, verbose_name=_('car type'), null=True, blank=True)

    def __str__(self):
        return f"{self.customer} {self.license_plate} {self.model_make}"

class Service(models.Model):
    name = models.CharField(_('service name'),max_length=255)
    price = models.DecimalField(_('price'),max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name}: {self.price}$"

class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name=_('car'))
    date = models.DateTimeField(_('date'), null=True, blank=True, db_index=True)
    order_total = models.DecimalField(_('order total'),max_digits=8, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.car}: {self.order_total}$"

class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_lines', verbose_name=_('order'))
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name=_('service'))
    quantity = models.PositiveIntegerField(_('quantity'), default=1)

    @property
    def line_total(self):
        return self.service.price * self.quantity

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.order.order_total = sum(line.line_total for line in self.order.order_lines.all())
        self.order.save()

    def __str__(self):
        return f"{self.order.car}: {self.service.name} ({self.quantity}) - {self.line_total}$"
