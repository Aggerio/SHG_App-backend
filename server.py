from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv('MONGO_URI')
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.get_database("shg_site")

app = Flask(__name__)

# Endpoint for retrieving all users
@app.route('/all_users', methods=['GET'])
def get_users():
    try:
        collection = db.get_collection("Users")
        documents = list(collection.find())
        for i in documents:
            i['_id'] = str(i['_id'])
        users = list(documents)
        return jsonify(users)
    except Exception as e:
        print(f"The following exception occured: {e}")
        return jsonify({"data": "None"})


# Endpoint for retrieving all products
@app.route('/all_products', methods=['GET'])
def get_products():
    try:
        collection = db.get_collection("Products")
        documents = list(collection.find())
        for i in documents:
            i['_id'] = str(i['_id'])
        products = list(documents)
        return jsonify(products)
    except Exception as e:
        print(f"The following exception occured: {e}")
        return jsonify({"data": "None"})

# Endpoint for retrieving all SHGs
@app.route('/all_shgs', methods=['GET'])
def get_shgs():
    try:
        collection = db.get_collection("SHGs")
        documents = list(collection.find())
        for i in documents:
            i['_id'] = str(i['_id'])
        shgs= list(documents)
        return jsonify(shgs)
    except Exception as e:
        print(f"The following exception occured: {e}")
        return jsonify({"data": "None"})

# Endpoint for retrieving all posts
@app.route('/all_posts', methods=['GET'])
def get_posts():
    try:
        collection = db.get_collection("Posts")
        documents = list(collection.find())
        for i in documents:
            i['_id'] = str(i['_id'])
        posts = list(documents)
        return jsonify(posts)
    except Exception as e:
        print(f"The following exception occured: {e}")
        return jsonify({"data": "None"})

# Endpoint for retrieving all contracts
@app.route('/all_contracts', methods=['GET'])
def get_contracts():
    try:
        collection = db.get_collection("Contracts")
        documents = list(collection.find())
        for i in documents:
            i['_id'] = str(i['_id'])
        contracts = list(documents)
        return jsonify(contracts)
    except Exception as e:
        print(f"The following exception occured: {e}")
        return jsonify({"data": "None"})

@app.route('/product_category', methods=['POST'])
def get_category_products():
    # requires json of the below type
    # {"category": "Textile"}
    if request.is_json:
        data = request.get_json()  # Parse JSON data
        category = data.get('category')
        try:
            collection = db.get_collection("Products")
            query = {"product_category": category}
            products = list(collection.find(query))
            for i in products:
                i['_id'] = str(i['_id'])
            return jsonify(products)
        except Exception as e:
            print(f"the following exception occured: {e}")
            return jsonify({"data": "none"})
    else:
        return jsonify({'error': 'Request must be in JSON format'}), 400

@app.route('/organisation_posts', methods=['POST'])
def get_organisation_posts():
    # requires json of the below type
    # {"organisation": "Sakhi Mahila Mandal"}
    if request.is_json:
        data = request.get_json()  # Parse JSON data
        organisation = data.get('organisation')
        try:
            collection = db.get_collection("SHGs")
            query = {"organisation_name": organisation}
            organis = collection.find_one(query)
            print(organis)
            if organis is not None and len(organis) != 0:
                return_posts = []
                posts = organis['organisation_posts']
                collection = db.get_collection('Posts')
                for i in posts:
                    query = {'post_id': i}
                    temp = collection.find_one(query)
                    temp['_id'] = str(temp['_id'])
                    return_posts.append(temp)
                return jsonify(return_posts)
            else:
                print("No posts found by the organisation")
                return jsonify({"data": "none"})
        except Exception as e:
            print(f"the following exception occured: {e}")
            return jsonify({"data": "none"})
    else:
        return jsonify({'error': 'Request must be in JSON format'}), 400


if __name__ == '__main__':
    app.run(debug=True)