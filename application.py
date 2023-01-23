from flask import Flask, request
from constants import all_products


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/products', methods=['GET'])
def get_all_products():
    return all_products, 200


@app.route('/products', methods=['POST'])
def insert_product():
    print(request.json)
    return {'Message': 'Operation completed!'}, 200


if __name__ == "__main__":
    app.run()
