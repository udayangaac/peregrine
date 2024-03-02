from marshmallow import Schema, fields

class SKUSchema(Schema):
    id = fields.Integer()
    product_code = fields.String()
    size = fields.String()
    color = fields.String()
    material = fields.String()

sku_schema = SKUSchema()
skus_schema = SKUSchema(many=True)