
class Restaurant:
    restaurants = []

    def __init__(self, code, name, country):
        self.code = code
        self.name = name
        self.country = country
        self._status = False
        self._ratings = []
        self.restaurants.append(self)

    def __str__(self):
        return f"{self.code} {self.name} {self.country} {self._status}"

    @property
    def status(self):
        return "Active" if self._status else "Inactive"

    @property
    def rating_average(self):
        if not self._ratings:
            return "- No Reviews Found"
        rating_sum = sum(review.rating for review in self._ratings)
        ratings = len(self._ratings)
        average = round(rating_sum / ratings, 1)
        return average

    @classmethod
    def list_restaurants(cls):
        for restaurant in cls.restaurants:
            print(f"Restaurant Code: {restaurant.code}\n"
                  f"Restaurant Name: {restaurant.name}\n"
                  f"Restaurant Country: {restaurant.country}\n"
                  f"Restaurant Rating: {restaurant.rating_average}\n"
                  f"Restaurant Status: {restaurant.status}\n")

    @classmethod
    def activate_restaurant(cls, code):
        for restaurant in cls.restaurants:
            if restaurant.code == code:
                restaurant.alter_restaurant_status()
                return restaurant.name, restaurant.status
        return code

    @classmethod
    def rate_restaurant(cls, code, client, rating):
        restaurant_found = False
        for restaurant in cls.restaurants:
            if restaurant.code == code:
                restaurant_found = True
                restaurant.receive_rating(client, rating)
        if not restaurant_found:
            return code

    def receive_rating(self, client, rating):
        if rating > 5:
            rating = 5
        if rating < 0:
            rating = 0
        rating = Ratings(client, rating)
        self._ratings.append(rating)

    def alter_restaurant_status(self):
        self._status = not self._status


class Ratings:

    def __init__(self, client, rating):
        self._client = client
        self.rating = rating
