from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice
from uuid import uuid4
import os
from decimal import Decimal
import tempfile

os.environ["INVOICE_LANG"] = "es"

def generate_invoice(data):
    provider = Provider('Tu Empresa', bank_account='123456', bank_name='Banco Inventado')
    client = Client(data.client.name, address=data.client.address)
    creator = Creator('Sistema de Facturación API')

    invoice = Invoice(client, provider, creator)

    for item in data.items:
        # Convert to float first, then to string with locale-independent format
        quantity = float(item.quantity)
        unit_price = float(item.unit_price)
        invoice.add_item(Item(
            description=item.name,
            count=quantity,
            price=unit_price
        ))

    # Guardar en la carpeta /pdf de la aplicación
    pdf_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pdf')
    
    # Asegurarse que la carpeta existe
    os.makedirs(pdf_dir, exist_ok=True)
    
    filename = os.path.join(pdf_dir, f"factura_{uuid4().hex}.pdf")
    
    pdf = SimpleInvoice(invoice)
    pdf.gen(filename, generate_qr_code=False)

    return filename
