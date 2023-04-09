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




# Necesito inicializarlo
if __name__ == '__main__':
    app.run(debug=True, port=4000)

