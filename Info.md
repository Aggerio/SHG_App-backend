User model --> 

user_id,
user_name,
user_email, 
user_organization(optional),
user_location


Product Model --> 

product_id, 
product_serial number,
product_name, 
product_price, 
product_rating, 
product_organisation,
product_description,
product_weight,
product_dimension,
product_img_link,
product_category


SHG model --> 

organisation_id, 
organisation_name, 
organisation_location, 
organisation_num_people, 
organisation_posts,
organisation_representative_name,
organisation_collection_listing_id


Post model --> 

post_id,
organisation_id, 
post_header, 
post_date,
post_description,
post_img_link,

Contracts model --> 

contract_id, 
contract_organisation_name,
contract_header,
contract_description,
contract_price,
contract_img_link,
contract_status

All product categories = [ Handicraft, Textile, Herbal_Ayurveda, Furniture, Food ]
