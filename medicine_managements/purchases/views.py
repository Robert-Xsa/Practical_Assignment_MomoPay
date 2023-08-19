from django.shortcuts import render

# Create your views here.
from .forms import InvoiceForm
from django.shortcuts import render, redirect
from .models import MedicineStock


def add_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save()
            # Update medicine stock quantities
            for medicine_stock in form.cleaned_data['medicines']:
                medicine_stock.QUANTITY -= 1  # Adjust quantity as needed
                medicine_stock.save()
            # Additional logic for processing the invoice
            return redirect('success')  # Redirect to a success page
    else:
        form = InvoiceForm()
    
    return render(request, 'add_invoice.html', {'form': form})

