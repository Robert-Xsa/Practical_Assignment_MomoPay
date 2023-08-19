from django.contrib import admin
from purchases.models import Customer, Invoice, Medicine, MedicineStock, Purchase, Supplier

# Register your models here.
admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(Medicine)
admin.site.register(MedicineStock)
admin.site.register(Purchase)
admin.site.register(Supplier)
