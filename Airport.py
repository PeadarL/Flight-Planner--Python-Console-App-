class Airport(object):

    def __init__(self, id, name, country, city, latitude, longitude):
        self.name = name
        self.id = id
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.country = country
        self.city = city

    def get_details(self):
        print(self.name, "Airport, in ", self.city, ", is in the country of ", self.country)

    def get_country(self):
        return self.country

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

    def __str__(self):
        return "{}".format(self.id)

    def __repr__(self):
        return "{}".format(self.id)
