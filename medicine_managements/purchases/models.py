from django.db import models

# Create your models here.
class Customer(models.Model):
    ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=20)
    CONTACT_NUMBER = models.CharField(max_length=10)
    ADDRESS = models.CharField(max_length=100)
    DOCTOR_NAME = models.CharField(max_length=20)
    DOCTOR_ADDRESS = models.CharField(max_length=100)

    class Meta:
        db_table = 'customers'
    
class Invoice(models.Model):
    INVOICE_ID = models.AutoField(primary_key=True)
    NET_TOTAL = models.FloatField(default=0)
    INVOICE_DATE = models.DateField(auto_now_add=True)
    CUSTOMER_ID = models.IntegerField()
    TOTAL_AMOUNT = models.FloatField()
    TOTAL_DISCOUNT = models.FloatField()

    class Meta:
        db_table = 'invoices'
        
class Medicine(models.Model):
    ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=100)
    PACKING = models.CharField(max_length=20)
    GENERIC_NAME = models.CharField(max_length=100)
    SUPPLIER_NAME = models.CharField(max_length=100)

    class Meta:
        db_table = 'medicines'
        
class MedicineStock(models.Model):
    ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=100)
    BATCH_ID = models.CharField(max_length=20, unique = True)
    EXPIRY_DATE = models.CharField(max_length=10)
    QUANTITY = models.IntegerField()
    MRP = models.FloatField()
    RATE = models.FloatField()

    class Meta:
        db_table = 'medicines_stock'
        
class Purchase(models.Model):
    VOUCHER_NUMBER = models.AutoField(primary_key=True)
    SUPPLIER_NAME = models.CharField(max_length=100)
    INVOICE_NUMBER = models.IntegerField()
    PURCHASE_DATE = models.CharField(max_length=10)
    TOTAL_AMOUNT = models.FloatField()
    PAYMENT_STATUS = models.CharField(max_length=20)

    class Meta:
        db_table = 'purchases'
        
class Supplier(models.Model):
    ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=100)
    EMAIL = models.CharField(max_length=100)
    CONTACT_NUMBER = models.CharField(max_length=10)
    ADDRESS = models.CharField(max_length=100)

    class Meta:
        db_table = 'suppliers'
        

