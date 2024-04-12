from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv('MONGO_URI')
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

users = [
  {
    "user_id": 1,
    "user_name": "Aarav Sharma",
    "user_email": "aarav.sharma@example.com",
    "user_organization": "Sakhi Mahila Mandal",
    "user_location": "Mumbai"
  },
  {
    "user_id": 2,
    "user_name": "Nisha Gupta",
    "user_email": "nisha.gupta@example.com",
    "user_organization": None,
    "user_location": "Delhi"
  },
  {
    "user_id": 3,
    "user_name": "Rohan Patel",
    "user_email": "rohan.patel@example.com",
    "user_organization": "Stree Shakti Samuh",
    "user_location": "Ahmedabad"
  }
]

products = [
  {
    "product_id": 1,
    "product_serial_number": "ABC123",
    "product_name": "Handwoven Silk Saree",
    "product_price": 2500.0,
    "product_rating": 4.8,
    "product_organisation": "Sakhi Mahila Mandal",
    "product_description": "Beautifully handwoven silk saree from Banaras",
    "product_weight": 0.8,
    "product_category": "Textile",
    "product_dimension": "6x2x2",
    "product_img_link": "https://example.com/saree.jpg"
  },
  {
    "product_id": 2,
    "product_serial_number": "DEF456",
    "product_name": "Terracotta Pottery Set",
    "product_price": 1200.0,
    "product_rating": 4.5,
    "product_organisation": "Stree Shakti Samuh",
    "product_description": "Handcrafted terracotta pottery set from Kutch",
    "product_category": "Handicraft",
    "product_weight": 3.2,
    "product_dimension": "10x8x6",
    "product_img_link": "https://example.com/pottery.jpg"
  },
  {
    "product_id": 3,
    "product_serial_number": "GHI789",
    "product_name": "Jute Handwoven Rug",
    "product_price": 1800.0,
    "product_rating": 4.2,
    "product_organisation": "Sakhi Mahila Mandal",
    "product_description": "Beautiful handwoven jute rug from West Bengal",
    "product_category": "Handicraft",
    "product_weight": 2.5,
    "product_dimension": "8x4x1",
    "product_img_link": "https://example.com/rug.jpg"
  }
]

shg = [
  {
    "organisation_id": 1,
    "organisation_name": "Sakhi Mahila Mandal",
    "organisation_location": "Mumbai",
    "organisation_num_people": 25,
    "organisation_posts": [1, 3],
    "organisation_representative_name": "Priya Desai",
    "organisation_collection_listing_id": 101
  },
  {
    "organisation_id": 2,
    "organisation_name": "Stree Shakti Samuh",
    "organisation_location": "Ahmedabad",
    "organisation_num_people": 18,
    "organisation_posts": [2],
    "organisation_representative_name": "Rani Patel",
    "organisation_collection_listing_id": 102
  },
  {
    "organisation_id": 3,
    "organisation_name": "Mahila Swayam Sahayata Gat",
    "organisation_location": "Pune",
    "organisation_num_people": 32,
    "organisation_posts": [],
    "organisation_representative_name": "Sita Kulkarni",
    "organisation_collection_listing_id": 103
  }
]

posts = [
  {
    "post_id": 1,
    "organisation_id": 1,
    "post_header": "New Saree Collection",
    "post_description": "Check out our latest collection of handwoven silk sarees!",
    "post_img_link": "https://example.com/saree_collection.jpg",
    "post_data": "2023-04-15"
  },
  {

    "post_id": 2,
    "organisation_id": 2,
    "post_header": "Pottery Exhibition",
    "post_description": "Our terracotta pottery will be showcased at the local exhibition this weekend.",
    "post_img_link": "https://example.com/pottery_exhibition.jpg",
    "post_data": "2023-04-20"
  },
  {

    "post_id": 3,
    "organisation_id": 1,
    "post_header": "Jute Rug Sale",
    "post_description": "Get 20% off on our handwoven jute rugs for a limited time!",
    "post_img_link": "https://example.com/rug_sale.jpg",
    "post_data": "2023-04-10"
  }
]


db = client.get_database("shg_site")

# users_collection = db.get_collection("Users")
# users_collection.insert_one({"user_id": 4, "user_name": "Aryaman Chandra","user_email": "aryamanow@gmail.com", "user_organization": None, "user_location": "Delhi"})
# users_collection.insert_many(users)

# products_collection = db.get_collection("Products")
# products_collection.insert_many(products)

# shgs_collection = db.get_collection("SHGs")
# shgs_collection.insert_many(shg)

# posts_collection = db.get_collection("Posts")
# posts_collection.insert_many(posts)

contracts = [
  {
    "contract_id": 1,
    "contract_organisation_name": "Tata Sustainability Initiative",
    "contract_header": "Women Empowerment through Skill Development",
    "contract_description": "Provide vocational training and entrepreneurship opportunities for women in rural areas to promote gender equality and economic empowerment (SDG 5: Gender Equality).",
    "contract_price": 2500000,
    "contract_img_link": "https://example.com/contract1.jpg"
  },
  {
    "contract_id": 2,
    "contract_organisation_name": "Reliance Renewable Energy Program",
    "contract_header": "200 wooden chairs",
    "contract_description": "There are 200 wooden chairs required for a new office that is being inaugurated in Pune",
    "contract_price": 3200000,
    "contract_img_link": "https://example.com/contract2.jpg"
  },
  {
    "contract_id": 3,
    "contract_organisation_name": "Wipro Environment Initiative",
    "contract_header": "30 women chefs are required for mass kitchen ",
    "contract_description": "Engage 30 women chefs from self-help groups to operate a mass kitchen that will provide nutritious meals to underprivileged communities. The initiative aims to promote gender equality, decent work opportunities, and zero hunger (SDGs 5, 8, and 2). The women chefs will receive training, fair wages, and support in developing entrepreneurial skills.",
    "contract_price": 1800000,
    "contract_img_link": "https://example.com/contract3.jpg"
  }
]

# contracts_collection = db.get_collection("Contracts")
# contracts_collection.insert_many(contracts)
