import pymongo
from restaurant import Restaurant

client = pymongo.MongoClient("localhost", 27017)


class RestaurantDatabase:
    restaurant_db = client.Express_Flavour
    restaurant_col = restaurant_db.Restaurants

    @classmethod
    def insert_restaurant_db(cls, restaurant_dict):
        restaurant_code = restaurant_dict["code"]
        restaurant_name = restaurant_dict["name"]
        restaurant_country = restaurant_dict["country"]
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
    def update_restaurant_status_db(cls, restaurant_code, updated_value):
        cls.restaurant_col.find_one_and_update({"Code": restaurant_code},
                                               {"$set": {"Status": updated_value}})
        return

    @classmethod
    def update_restaurant_ratings_db(cls, restaurant_code, updated_value):
        rating_total = 0
        restaurant = cls.restaurant_col.find_one_and_update({"Code": restaurant_code},
                                                            {"$push": {"Ratings": updated_value}},
                                                            return_document=pymongo.ReturnDocument.AFTER)
        if restaurant is not None:
            for rating in restaurant["Ratings"]:
                value = rating["Rating"]
                rating_total += value
                rating_avg = rating_total / len(restaurant["Ratings"])
                cls.restaurant_col.find_one_and_update({"Code": restaurant_code},
                                                       {"$set": {"Rating_avg": rating_avg}})
            return rating_total
