from pydantic import BaseModel, Field
from typing import List
from decimal import Decimal

class ItemDTO(BaseModel):
    name: str
    quantity: Decimal = Field(gt=0)
    unit_price: Decimal = Field(gt=0)

class ClientDTO(BaseModel):
    name: str
    address: str

class InvoiceRequest(BaseModel):
    client: ClientDTO
    items: List[ItemDTO]
    invoice_type: str  # 'A' o 'B'
