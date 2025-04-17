from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice
from uuid import uuid4
import os
from decimal import Decimal
import tempfile

# Configuración de factura
os.environ["INVOICE_LANG"] = "es"
os.environ["INVOICE_CURRENCY"] = "$"
os.environ["INVOICE_CURRENCY_LOCALE"] = "en_US.UTF-8"

def generate_invoice(data):
    provider = Provider('Tu Empresa', bank_account='123456', bank_name='Banco Inventado')
    client = Client(data.client.name, address=data.client.address)
    creator = Creator('Sistema de Facturación API')

    invoice = Invoice(client, provider, creator)
    
    invoice.currency = "$"
    invoice.currency_locale = "en_US.UTF-8"
    
    for item in data.items:
        # Convert to float first
        quantity = float(item.quantity)
        unit_price = float(item.unit_price)
        
        item_obj = Item(
            description=item.name,
            count=quantity,
            price=unit_price,
            unit=""
        )
        
        invoice.add_item(item_obj)
    
    pdf_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pdf')
    os.makedirs(pdf_dir, exist_ok=True)
    
    filename = os.path.join(pdf_dir, f"factura_{uuid4().hex}.pdf")
    
    pdf = SimpleInvoice(invoice)
    
    pdf.invoice.currency_locale = invoice.currency_locale
    pdf.invoice.currency = invoice.currency
    
    pdf.gen(filename, generate_qr_code=False)

    return filename
