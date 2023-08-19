from django.core.management.base import BaseCommand
from django.conf import settings
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from purchases.models import Purchase, Invoice

class Command(BaseCommand):
    help = 'Generate invoices based on completed purchase orders'

    def handle(self, *args, **options):
        purchases = Purchase.objects.filter(payment_status='Completed')
        
        for purchase in purchases:
            invoice = Invoice.objects.create(
                CUSTOMER_ID=purchase.CUSTOMER_ID,
                TOTAL_AMOUNT=purchase.TOTAL_AMOUNT,
                TOTAL_DISCOUNT=purchase.TOTAL_DISCOUNT
            )
            
            # Generate PDF invoice
            pdf_content = self.generate_pdf_invoice(invoice)
            # Save or send the PDF content as needed
            
    def generate_pdf_invoice(self, invoice):
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)

        p.drawString(100, 750, 'Invoice')
        p.drawString(100, 700, f'Customer ID: {invoice.CUSTOMER_ID}')
        p.drawString(100, 650, f'Total Amount: {invoice.TOTAL_AMOUNT}')
        p.drawString(100, 600, f'Total Discount: {invoice.TOTAL_DISCOUNT}')

        p.save()
        buffer.seek(0)
        return buffer.read()

