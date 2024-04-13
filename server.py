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
print("Initiased db successful ")
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

@app.route('/get_user_data', methods = ['POST'])
def get_user_data():
    # requires json of the below type
    # {"user_email": "aryamanow@gmail.com"}
    if request.is_json:
        data = request.get_json()
        user_email = data.get('user_email')
        try:
            collection = db.get_collection('Users')
            query = {'user_email': user_email}
            user_info = collection.find_one(query)
            print("User info: ", user_info)
            user_info['_id'] = str(user_info['_id'])
            return jsonify(user_info)
        except Exception as e:
            print(f"The following exception occured: {e}")
            return jsonify({"data": "none"})


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

@app.route('/create_post', methods=['POST'])
def create_post():
    # requires json of the below type
    #   {
    #     "organisation_name": "Mahila Swayam Sahayata Gat",
    #     "post_header": "Pottery Exhibition",
    #     "post_description": "Our terracotta pottery will be showcased at the local exhibition this weekend.",
    #     "post_img_link": "https://example.com/pottery_exhibition.jpg",
    #     "post_date": "2023-04-20"
    #   }

    # get the organisation id from organisation name
    # add post and update SHGs organisation_posts with the new post 
    if request.is_json:
        data = request.get_json()  # Parse JSON data
        organisation_name = data.get('organisation_name')
        post_header = data.get('post_header')
        post_description = data.get('post_description')
        post_img_link = data.get('post_img_link')
        post_date = data.get("post_date")
        try:
            shgs_collection = db.get_collection("SHGs")

            query = {"organisation_name": organisation_name}
            organis = shgs_collection.find_one(query)

            posts_collection = db.get_collection('Posts')

            if organis is not None and len(organis) != 0:
                organisation_id = organis['organisation_id']
                organisation_profile_picture = organis['organisation_profile_picture']
                organisation_posts = organis['organisation_posts']

                post_id = posts_collection.count_documents({}) + 1
                final_post = {
                    "post_id": post_id,
                    "organisation_id": organisation_id,
                    "post_header": post_header,
                    "post_description": post_description,
                    "post_img_link": post_img_link,
                    "post_date": post_date,
                    "organisation_profile_picture": organisation_profile_picture
                }
                posts_collection.insert_one(final_post)
                organisation_posts.append(post_id)
                shgs_collection.update_one({"organisation_id": organisation_id}, {"$set" : {"organisation_posts": organisation_posts}})
                return jsonify({"insertion":"successful" })
            else:
                print("No posts found by the organisation")
                return jsonify({"data": "none"})
        except Exception as e:
            print(f"the following exception occured: {e}")
            return jsonify({"data": "none"})
    else:
        return jsonify({'error': 'Request must be in JSON format'}), 400

@app.route('/create_product', methods = ['POST'])
def create_product():
    # the resulting json should be of the format: 
    # {
    #   "product_serial_number": "ABC123",
    #   "product_name": "Handwoven Silk Saree",
    #   "product_price": 2500.0,
    #   "product_rating": 4.8,
    #   "product_organisation": "Sakhi Mahila Mandal",
    #   "product_description": "Beautifully handwoven silk saree from Banaras",
    #   "product_weight": 0.8,
    #   "product_category": "Textile",
    #   "product_dimension": "6x2x2",
    #   "product_img_link": "https://example.com/saree.jpg"
    # },
    if request.is_json:
        data = request.get_json()
        product_serial_number = data.get('product_serial_number')
        product_name = data.get('product_name')
        product_price = data.get('product_price')
        product_rating = data.get('product_rating')
        product_organisation = data.get('product_organisation')
        product_description = data.get('product_description')
        product_weight = data.get('product_weight')
        product_category = data.get('product_category')
        product_dimension = data.get('product_dimension')
        product_img_link = data.get('product_img_link')

        products_collection = db.get_collection('Products')


    else:
        return jsonify({'error': 'Request must be in JSON format'}), 400

if __name__ == '__main__':
    app.run(debug=True)