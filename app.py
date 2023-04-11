from flask import Flask, jsonify, request

# mi aplicación del servidor
app = Flask(__name__)

# Importar la lista de usuarios que tenermos en products.py
from products import products

# Creamos una ruta 
@app.route('/products')
# funtion que retorna un array
def getProducts():
    return jsonify(products)
    # Retornamos un objeto que tiene la lista de productos
    # return jsonify({"Products": products})

# @app.route('/products/<product_name>')
# @app.route('/products/:product_name')
@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if(product["name"] == product_name)]
    if(len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": "Product not found"})

# Registrar product
@app.route("/products", methods=["POST"])
def postProduct():
    new_product = {
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"]
    }
    products.append(new_product)
    return jsonify({"message": "Product added successfully", "products": products})

# Editar producto
@app.route("/products/<string:product_name>", methods=["PUT"])
def editProduct(product_name):
    productsFound = [product for product in products if(product["name"] == product_name)]
    if(len(productsFound) > 0):
        productsFound[0]["name"] = request.json["name"]
        productsFound[0]["price"] = request.json["price"]
        productsFound[0]["quantity"] = request.json["quantity"]
        return jsonify({"message": "Product edit successfully", "products": productsFound[0]})
    return jsonify({"message": "Product Not found"})

# Eliminar producto
@app.route("/products/<string:product_name>", methods=["DELETE"])
def deleteProduct(product_name):
    productFound = [product for product in products if(product["name"] == product_name)]
    if(len(productFound[0]) > 0):
        products.remove(productFound[0])
        return jsonify({"message": "Producto eliminado", "product": productFound[0]})
    return jsonify({"message": "Producto Not found"})

# Necesito inicializarlo
if __name__ == '__main__':
    app.run(debug=True, port=4000)

