from flask import jsonify, request
from app import app, db
from app.models import SKU
from app.schemas import sku_schema, skus_schema

# Create a SKU
@app.route('/sku', methods=['POST'])
def create_sku():
    data = request.json
    sku = SKU(product_code=data['product_code'], size=data['size'], color=data['color'], material=data['material'])
    db.session.add(sku)
    db.session.commit()
    return sku_schema.jsonify(sku), 201

# Get all SKUs
@app.route('/sku', methods=['GET'])
def get_skus():
    all_skus = SKU.query.all()
    result = skus_schema.dump(all_skus)
    return jsonify(result)

# Get a single SKU
@app.route('/sku/<int:id>', methods=['GET'])
def get_sku(id):
    sku = SKU.query.get_or_404(id)
    return sku_schema.jsonify(sku)

# Update a SKU
@app.route('/sku/<int:id>', methods=['PUT'])
def update_sku(id):
    sku = SKU.query.get_or_404(id)
    data = request.json
    sku.product_code = data['product_code']
    sku.size = data['size']
    sku.color = data['color']
    sku.material = data['material']
    db.session.commit()
    return sku_schema.jsonify(sku)

# Delete a SKU
@app.route('/sku/<int:id>', methods=['DELETE'])
def delete_sku(id):
    sku = SKU.query.get_or_404(id)
    db.session.delete(sku)
    db.session.commit()
    return jsonify({'message': 'SKU deleted successfully'})
