class Restaurant:

    def __init__(self, code, name, country):
        self.code = code
        self.name = name
        self.country = country
        self._status = False
        self._ratings = []

    def __str__(self):
        return f"{self.code} {self.name} {self.country} {self.status}"

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

    @property
    def dict_builder(self):
        return {"Code": self.code,
                "Name": self.name,
                "Country": self.country,
                "Status": self.status,
                "Rating_avg": self.rating_average}

    def receive_rating(self, client, rating):
        if rating > 5:
            rating = 5
        if rating < 0:
            rating = 0
        rating = Ratings(client, rating)
        self._ratings.append(rating)

    def activate_restaurant(self):
        self._status = True

    def deactivate_restaurant(self):
        self._status = False


class Ratings:

    def __init__(self, client, rating):
        self._client = client
        self.rating = rating
