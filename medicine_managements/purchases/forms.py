# forms.py
from django import forms
from .models import Invoice, MedicineStock

class InvoiceForm(forms.ModelForm):
    medicines = forms.ModelMultipleChoiceField(queryset=MedicineStock.objects.all())

    class Meta:
        model = Invoice
        fields = ['CUSTOMER_ID', 'medicines', 'TOTAL_AMOUNT', 'TOTAL_DISCOUNT']

