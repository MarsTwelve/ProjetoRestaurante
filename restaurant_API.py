from fastapi import FastAPI
from pydantic import BaseModel
from restaurant import Restaurant
from Restaurant_database import RestaurantDatabase


def show_restaurants(restaurant_info):
    return ("Restaurant Name:", restaurant_info['Name'], "-" 
            "Restaurant Country:", restaurant_info['Country'], "-",
            "Restaurant Status:", restaurant_info['Status'], "-",
            "Restaurant Rating Average:", restaurant_info['Rating_avg'])


app = FastAPI(title="Express Flavour",
              description="A restaurant app thingy",
              summary="You can see and review restaurants",
              version="WIP",
              terms_of_service="https://express-flavour.com/tos",
              contact={"name": "Mars",
                       "url": "https://github.com/MarsTwelve/",
                       "email": "matheusfer33@hotmail.com"})


class RestaurantModel(BaseModel):
    code: int
    name: str
    country: str


@app.post("/express-flavour/restaurants/new-restaurant")
def add_restaurant(restaurant: RestaurantModel):
    RestaurantDatabase.insert_restaurant_db(restaurant.model_dump())
    return restaurant.model_dump()


@app.get("/express-flavour/restaurants")
def show_all_restaurants():
    restaurant_info = RestaurantDatabase.find_restaurant_db()
    for restaurant in restaurant_info:
        yield show_restaurants(restaurant)


@app.get("/express-flavour/restaurants/restaurant/{restaurant-code}")
def show_restaurant_info(restaurant_code: int):
    restaurant_info = RestaurantDatabase.find_restaurant_db(restaurant_code)
    return show_restaurants(restaurant_info)


@app.put("/express-flavour/restaurants/restaurant/activate/{restaurant-code}")
def activate_restaurant(restaurant_code: int, status: bool):
    restaurant_info = RestaurantDatabase.find_restaurant_db(restaurant_code)
    restaurant_instance = Restaurant(restaurant_info["Code"], restaurant_info["Name"], restaurant_info["Country"])
    if status:
        restaurant_instance.activate_restaurant()
    else:
        restaurant_instance.deactivate_restaurant()
    RestaurantDatabase.update_restaurant_status_db(restaurant_info["Code"], restaurant_instance.status)
    return restaurant_instance.status


@app.put("/express-flavour/restaurants/restaurant/add-rating")
def add_rating(restaurant_code: int, client: str, rating: float):
    restaurant_info = RestaurantDatabase.find_restaurant_db(restaurant_code)
    restaurant_instance = Restaurant(restaurant_info["Code"], restaurant_info["Name"], restaurant_info["Country"])
    restaurant_rating = restaurant_instance.receive_rating(client, rating)
    RestaurantDatabase.update_restaurant_ratings_db(restaurant_code, restaurant_rating)
    return restaurant_rating
