import pymongo
from restaurant import Restaurant

client = pymongo.MongoClient("localhost", 27017)


class RestaurantDatabase:
    restaurant_db = client.Express_Flavour
    restaurant_col = restaurant_db.Restaurants

    @classmethod
    def insert_restaurant_db(cls, restaurant_dict):
        restaurant_code = restaurant_dict["restaurant_code"]
        restaurant_name = restaurant_dict["restaurant_name"]
        restaurant_country = restaurant_dict["restaurant_country"]
        restaurant_obj = Restaurant(restaurant_code, restaurant_name, restaurant_country)

        cls.restaurant_col.insert_one(restaurant_obj.dict_builder)

    @classmethod
    def find_restaurant_db(cls, restaurant_code=None):
        restaurant_list = []
        if restaurant_code is None:
            restaurants = cls.restaurant_col.find()
            for restaurant in restaurants:
                restaurant_list.append(restaurant)
            return restaurant_list
        restaurant = cls.restaurant_col.find_one({"Code": restaurant_code})
        return restaurant

    @classmethod
    def update_restaurant_db(cls, restaurant_code, field_name, updated_value):
        restaurant = cls.restaurant_col.find_one_and_update({"Code": restaurant_code},
                                                            {"$set": {field_name: updated_value}},
                                                            return_document=pymongo.ReturnDocument.AFTER)
        return restaurant
