import datetime
from app import db

class Product(db.Model):
    __tablename__= "products"

    id_product = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String, nullable=False)
    quantity_ = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __init__(self, product, price):
        self.product = product
        self.price = price
    
    def __repr__(self):
        return "<product %r>" % self.product

class ReceiptItem(db.Model):
    ___tablename__= "receipts_item"

    id_receipt_item = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    subtotal = db.Column(db.Integer, nullable=False)

    def __init__(self, product, quantiy, price, subtotal):
        self.product = product
        self.quantity = quantiy
        self.price = price
        self.subtotal = subtotal
    
    def __repr__(self):
        return "<receipt id: %r>" % self.id_receipt_item
    
class Receipt(db.Model):
    __tablename__ = "receipts"

    id_receipt = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime)
    total_to_pay = db.Column(db.Float)

    def __init__(self, date ,total_to_pay):
        self.date = date
        self.total_to_pay = total_to_pay

    def __repr__(self):
        return "<receipt id %r>" % self.id_receipt
