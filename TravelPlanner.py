from math import pi, cos, sin, acos
import itertools
from FileReader import FileReader


class TravelPlanner:

    @staticmethod
    def distance_between_airports(code1, code2):
        def radians(angle):
            radian = angle * ((2 * pi) / 360)
            return radian

        def distance(long1, long2, lat1, lat2):
            radius = 6371
            long_rads1 = radians(long1)
            long_rads2 = radians(long2)
            lat_rads1 = radians(90 - lat1)
            lat_rads2 = radians(90 - lat2)  # Always Minus?
            formula_1 = sin(lat_rads1) * sin(lat_rads2) * cos(long_rads1 - long_rads2)
            formula_2 = cos(lat_rads1) * cos(lat_rads2)
            distance = acos(formula_1 + formula_2) * radius
            return distance

        return distance(code1.longitude, code2.longitude, code1.latitude, code2.latitude)

    @staticmethod
    def permutate_routes(airports):
        origin = airports[0]
        airports.remove(airports[0])  # permutates just the middle section  as the home airport remains the same.

        perms = list(itertools.permutations(airports))
        finals = []
        for perm in perms:
            perm = list(perm)
            perm.insert(0, origin)
            perm.append(origin)
            finals.append(perm)
        return finals

    @staticmethod
    def get_local_currency(airport):
        country = FileReader().airports.get(str(airport)).country
        home_currency = FileReader().currencies.get(country.upper()).code
        exchange_rate = FileReader().rates.get(home_currency).from_euro
        return exchange_rate

    @staticmethod
    def add_fuel(fuel_tank, distance, range):
        current_fuel = fuel_tank - distance
        added_fuel = range - current_fuel  # The Aircraft's fuel derived from it's range  minus its current fuel level.
        return added_fuel  # Missing fuel taken from above line is added to fill tank.

    @staticmethod
    def journey_details(aircraft, destinations):
        home = destinations[0]  # Home is the origin airport, ie the first input into destinations.
        origin_flights = destinations[0:]
        destination_flights = destinations[1:]  # destinations all but the home airport
        destination_flights.insert(len(destinations)-1,home)  # add home to the last destination
        range = aircraft.range
        fuel_tank = range  # maximum fuel is derived from the maximum range
        total_distance = 0
        cost = fuel_tank * TravelPlanner.get_local_currency(home)  # Fuel in litres times the local exchange in euro.
        for origin, destination in zip(origin_flights, destination_flights):
            try:
                distance = TravelPlanner.distance_between_airports(origin, destination)
                if distance > range:
                    print("Airplane is incapable of flying this route due to its range limitations.")
                    return None
                elif distance > fuel_tank:
                    added_fuel = TravelPlanner.add_fuel(fuel_tank, distance, range)
                    fuel_tank += added_fuel
                    cost += added_fuel * TravelPlanner.get_local_currency(origin)
                    fuel_tank -= distance
                else:
                    fuel_tank -= distance
                total_distance += distance
            except IndexError:
                pass
        print("Flying from", origin_flights, "to", destination_flights, "the total distance traveled is", "%.0f"
              % total_distance, "KM and the total cost is " "%.0f" % cost, "euro.")

    @staticmethod
    def get_shortest_route(destinations, aircraft):
        perms = TravelPlanner.permutate_routes(destinations)
        options = {}  # Create Empty Dictionary.
        total_distance = 0
        for x in range(len(perms)):
            for y in range(len(perms[x])):
                try:
                    distance = TravelPlanner.distance_between_airports(perms[x][y], perms[x][y + 1])
                    if distance < aircraft.range:
                        total_distance += distance
                        options[tuple(perms[x])] = total_distance
                    else:
                        return None
                except IndexError:
                    pass

        shortest = min(options, key=options.get)
        return shortest

    @staticmethod
    def plan_journey(reader):
        from UserInterface import get_airport
        print("Please enter an origin airport by its 3-letter code.")
        origin = get_airport(reader)
        destinations = []
        destinations.append(origin)
        print("Please enter up to 5 airport destinations by airport code. ")
        for num in range(1, 5):
            print("Enter Airport ", num, " or type 'done' to finish selecting airports. ")
            response = input().upper()
            if response.upper() == "DONE":
                break
            else:
                airport = reader.airports.get(response.upper())
                if airport is None:
                    print("Airport not found.")
                else:
                    destinations.append(airport)
        return destinations
