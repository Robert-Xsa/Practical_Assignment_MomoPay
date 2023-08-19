from django.db import models

# Create your models here.
class Medicine(models.Model):
    ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=100)
    PACKING = models.CharField(max_length=20)
    GENERIC_NAME = models.CharField(max_length=100)
    SUPPLIER_NAME = models.CharField(max_length=100)

    class Meta:
        db_table = 'medicines'
        
    def __str__(self):
        return self.NAME
    
class Supplier(models.Model):
    ID = models.AutoField(primary_key=True)
    Medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, verbose_name="MEDICINE NAME")
    NAME = models.CharField(max_length=100)
    EMAIL = models.EmailField()
    CONTACT_NUMBER = models.CharField(max_length=10)
    ADDRESS = models.CharField(max_length=100)

    class Meta:
        db_table = 'suppliers'
        
    def __str__(self):
        return self.NAME


class Customer(models.Model):
    ID = models.AutoField(primary_key=True)
    Supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="SUPPLIER NAME")
    NAME = models.CharField(max_length=20)
    CONTACT_NUMBER = models.CharField(max_length=10)
    ADDRESS = models.CharField(max_length=100)
    DOCTOR_NAME = models.CharField(max_length=20)
    DOCTOR_ADDRESS = models.CharField(max_length=100)

    class Meta:
        db_table = 'customers'
        
    def __str__(self):
        return self.NAME
    
class Invoice(models.Model):
    INVOICE_ID = models.AutoField(primary_key=True)
    NET_TOTAL = models.FloatField(default=0)
    INVOICE_DATE = models.DateField(auto_now_add=True)
    CUSTOMER_ID = models.IntegerField()
    TOTAL_AMOUNT = models.FloatField()
    TOTAL_DISCOUNT = models.FloatField()
    

    class Meta:
        db_table = 'invoices'
        
   
    def __str__(self):
        return f"Invoice ID: {self.INVOICE_ID}, Customer: {self.CUSTOMER_ID}, Amount: {self.TOTAL_AMOUNT}"
    

    
class MedicineStock(models.Model):
    ID = models.AutoField(primary_key=True)
    Medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, verbose_name="MEDICINE NAME")
    NAME = models.CharField(max_length=100)
    BATCH_ID = models.CharField(max_length=20, unique = True)
    EXPIRY_DATE = models.DateField()
    QUANTITY = models.IntegerField()
    MRP = models.FloatField()
    RATE = models.FloatField()

    class Meta:
        db_table = 'medicines_stock'
        
    def __str__(self):
        return self.NAME
    
    

        
class Purchase(models.Model):
    VOUCHER_NUMBER = models.AutoField(primary_key=True)
    medicines = models.ManyToManyField(MedicineStock)
    Supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="SUPPLIER NAME")
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="CUSTOMER NAME")
    INVOICE_NUMBER = models.IntegerField()
    PURCHASE_DATE = models.DateField()
    TOTAL_AMOUNT = models.FloatField()
    selection_1 = (
        ("C", "Completed"),
        ("N", "Not Completed"),  
    )
    PAYMENT_STATUS = models.CharField(max_length=20, choices = selection_1 )
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for medicine_stock in self.medicines.all():
            medicine_stock.QUANTITY += 1  # Update quantity, adjust as needed
            medicine_stock.save()
    

    class Meta:
        db_table = 'purchases'

    def __str__(self):
        return self.PAYMENT_STATUS
        
