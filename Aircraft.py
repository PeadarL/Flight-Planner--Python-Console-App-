class Aircraft(object):
    def __init__(self, code, aircrafttype, units, manufacturer, aircraftrange):
        self.code = code
        self.units = units
        self.range = aircraftrange
        self.manufacturer = manufacturer
        self.maxFuel = aircraftrange
        self.fuel = 0.0

        if units == 'imperial':
            self.imperial_to_metric()

    def get_code(self):  # returns aircraft code
        return self.code

    def get_manufacturer(self):  # returns aircraft maker
        return self.manufacturer

    def get_range(self):  # returns the max distance the aircraft can fly
        return self.range

    def get_details(self):  # returns aircraft details
        if self.maxFuel == 0:
            print("404 Plane not found")
            return False
        else:
            print(self)
            return True

    def __str__(self):
        return "Code: {} - Max Range {} - Manufacturer {}".format(self.code, self.maxFuel, self.manufacturer)

    def __repr__(self):
        return "Code: {} - Max Range {}KM - Manufacturer {}".format(self.code, self.maxFuel, self.manufacturer)

    def imperial_to_metric(self):  # used to convert all aircraft measurments into the metric system
        self.range *= 1.60934
        self.units = 'metric'
