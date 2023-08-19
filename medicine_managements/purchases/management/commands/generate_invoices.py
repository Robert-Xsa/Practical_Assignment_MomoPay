from django.core.management.base import BaseCommand
from django.conf import settings
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from purchases.models import Purchase, Invoice

class Command(BaseCommand):
    help = 'Generate invoices based on completed purchase orders'
    
    pdf_directory = 'D:/Gembe C++/Interview_coding/MomoPay_Interview/invoice_generated'
    

    def handle(self, *args, **options):
        purchases = Purchase.objects.filter(PAYMENT_STATUS='Completed')
        
        for purchase in purchases:
            invoice = Invoice.objects.create(
                VOUCHER_NUMBER=purchase.VOUCHER_NUMBER,
                SUPPLIER_NAME=purchase.SUPPLIER_NAME,
                INVOICE_NUMBER=purchase.INVOICE_NUMBER

                
            )
            
            # Generate PDF invoice
            pdf_content = self.generate_pdf_invoice(invoice)
            self.save_pdf_invoice(pdf_content, f'{self.pdf_directory}/invoice_{invoice.pk}.pdf')
            
    def generate_pdf_invoice(self, invoice):
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)

        p.drawString(100, 750, 'invoice')
        p.drawString(100, 700, f'Voucher Number: {invoice.VOUCHER_NUMBER}')
        p.drawString(100, 650, f'Supplier Name: {invoice.SUPPLIER_NAME}')
        p.drawString(100, 600, f'Invoice Number: {invoice.INVOICE_NUMBER}')

        p.save()
        buffer.seek(0)
        return buffer.read()

    def save_pdf_invoice(self, pdf_content, filename):
        with open(filename, 'wb') as f:
            f.write(pdf_content)
