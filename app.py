#usaremos el framework "Flask" pip install flask
#inportacion de flask
from flask import Flask, jsonify

#iniciamos flask y iniciamos la propiedad llamada name, evolviendo en una varable app
app = Flask(__name__)

from products import products

#ruta de prueba
@app.route('/ping')
    #cuando se ejecute la ruta de arriba de ejecuta la funcion de abajo
def ping():
    #para devolver una respuesta en formato json
    return jsonify({"message": "pong!"})

#definimos con que metodos vamos a trabajar la ruta con methods=['GET']
#por defecto se maneja este metodo, por lo que no es necesario

#obtener toda la lista de datos
@app.route('/products')
def getProducts():
    #se le envia la lista dentro de una propiedad, se le puede agregar mensajes y demas
    return jsonify({"message":"lista de productos","productos": products})

#obtener solo un dato por una propiedad id (en este caso el nombre)
#igualmente podemos definir que tipo de dato queremos como por ejemplo <string:products_name>
#esto para que solo se reciba este tipo de datos en la url
@app.route('/products/<string:product_name>')
def getProduct(product_name):
    #imprimo el nombre que recive de la url
    print(product_name)
    #se recorre el arreglo y traemos los productos que concidan con la variable product_name
    productsFound = [product for product in products if product['name'] == product_name]
    #validar si productsFound es igual a 0
    if (len(productsFound) > 0):
        #muestro un mensaje de recivido
        return jsonify({"message": "received","product": productsFound[0]})
    #mensaje si no encuentra un producto
    return jsonify({"message": "Product not found"})
if __name__ == '__main__':
    # ejecuta app en modo debug para que se reinicie cada que hagamos cambios
    # tambien se puede configurar el puerto que es lo que esta despues de la coma.
    app.run(debug=True, port=4000)
