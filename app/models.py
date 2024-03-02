from app import db

class SKU(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_code = db.Column(db.String(50), nullable=False)
    size = db.Column(db.String(20), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    material = db.Column(db.String(50), nullable=False)