from django.core.management.base import BaseCommand
from purchases.models import Purchase, Invoice, Customer
from django.core.exceptions import ObjectDoesNotExist
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

class Command(BaseCommand):
    help = 'Generate invoices for completed purchases'

    def handle(self, *args, **options):
        completed_purchases = Purchase.objects.filter(PAYMENT_STATUS='C')

        for purchase in completed_purchases:
            try:
                customer = Customer.objects.get(pk=purchase.Supplier.ID)
                
                invoice = Invoice.objects.create(
                    CUSTOMER_ID=customer.ID,
                    TOTAL_AMOUNT=purchase.TOTAL_AMOUNT,
                    TOTAL_DISCOUNT=0,
                )
                self.stdout.write(self.style.SUCCESS(f'Invoice created: {invoice}'))

                # Generate and print PDF invoice
                pdf_content = self.generate_pdf_invoice(invoice)
                self.print_pdf_invoice(pdf_content)
            except ObjectDoesNotExist:
                self.stdout.write(self.style.WARNING(f'No customer found for purchase with Supplier ID {purchase.Supplier.ID}'))

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

    def print_pdf_invoice(self, pdf_content):
        # Simulate printing by displaying PDF content length
        self.stdout.write(self.style.SUCCESS(f'PDF Invoice Content Length: {len(pdf_content)} bytes'))
