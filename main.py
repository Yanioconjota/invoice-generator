from fastapi import FastAPI
from fastapi.responses import FileResponse
from models import InvoiceRequest
from invoice_service import generate_invoice

app = FastAPI(title="Generador de Facturas")

@app.post("/generar-factura")
def generar_factura(data: InvoiceRequest):
    pdf_path = generate_invoice(data)
    return FileResponse(pdf_path, filename="factura.pdf", media_type="application/pdf")
