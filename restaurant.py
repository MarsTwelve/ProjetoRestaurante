class Restaurant:

    def __init__(self, code, name, country):
        self.code = code
        self.name = name
        self.country = country
        self._status = False

    def __str__(self):
        return f"{self.code} {self.name} {self.country} {self.status}"

    @property
    def status(self):
        return "Active" if self._status else "Inactive"

    @property
    def dict_builder(self):
        return {"Code": self.code,
                "Name": self.name,
                "Country": self.country,
                "Status": self.status,
                "Rating_avg": "- No Reviews Found",
                "Ratings": []}

    @staticmethod
    def receive_rating(client, rating):
        if rating > 5:
            rating = 5
        if rating < 0:
            rating = 0
        rating_instance = Ratings(client, rating)
        return rating_instance.ratings_dict

    def activate_restaurant(self):
        self._status = True

    def deactivate_restaurant(self):
        self._status = False


class Ratings:

    def __init__(self, client, rating):
        self._client = client
        self.rating = rating

    @property
    def ratings_dict(self):
        return {"Name": self._client, "Rating": self.rating}
