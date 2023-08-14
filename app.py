#usaremos el framework "Flask" pip install flask
#inportacion de flask
from flask import Flask, jsonify, request

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
#dentro de la url enviamos el remplazamos y enviamos el nombre del producto
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

#se puede usar la misma ruta ya que el metodo es diferente al metodo get anterior
#metodo de agregar por medio de un json
@app.route('/products' , methods=['POST'])
def addProduct():
    new_product = {
        #aqui recibira los datos para agregarlos al otro archivo
        "name":request.json['name'],
        "price":request.json['price'],
        "quantity":request.json['quantity']
    }
    #agregamos con append pasando en nuevo producto
    products.append(new_product)
    #mostrar en consola los datos que esta recibiedo
    print(request.json)
    #devolver un recibido,agregado y el listado para verificar que ha funcionado
    return jsonify({"message":"Received, Products Added SUccesfuly", "products":products})

#metodo de editar por medio un json po metodo put, opteniendo el nombre(id) de producto que queremos modificar
#dentro de la  url remplazamos por el producto que queremos actualizar
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    #hacemos un bucle para validar que ha encontrado un elemento
    productFound = [product for product in products if product['name'] == product_name]
    if(len(productFound) > 0):
        #si hay un resultado cambiamos los datos por los que vienen en el json de insomnia
        #en la posicion 0 (el resultado), cambie los datos que hay en ['<campo>']
        #por los datos que vienen del request.json['<campo>']
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            #devolvemos un mensaje y el producto modificado
            "message": "Product Updated",
            "products":productFound[0]
        })
    #si no encuentra el objeto a eliminar retorna un error
    return jsonify({"mesage": "Product Not Found"})

#ruta para eliminar un producto con metodo delete, escribimos en la ruta el nombre del producto que queremos eliminar
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    # hacemos un bucle para validar que ha encontrado un elemento
    productsFound = [product for product in products if product['name'] == product_name]
    #comprobar que porductsFound es mayo a 0, que la url a funcionado
    if(len(productsFound) > 0):
        #eliminamos el producto de la lista con la funcion remove
        products.remove(productsFound[0])
        #devolvemos el mensaje que mencione que el producto fue eliminado junto con la ista como ha quedado
        #sin el producto eliminado
        return jsonify({
            "message":"Product Deleted",
            "products": products
        })
    #retornamos un mensaje que mencione que no se encuentra el objeto llamado
    return jsonify({"message" : "Product Not Found"})

if __name__ == '__main__':
    # ejecuta app en modo debug para que se reinicie cada que hagamos cambios
    # tambien se puede configurar el puerto que es lo que esta despues de la coma.
    app.run(debug=True, port=4000)
