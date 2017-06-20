from TravelPlanner import TravelPlanner
from FileReader import FileReader
import unittest


class KnownDistances(unittest.TestCase):
    known_values = (("DUB", "JFK"), 5103.02675898737),\
                   (("DUB", "LTN"), 433.53285598902147),\
                   (("DUB", "AKL"), 18188.1723691295),\
                   (("DUB", "DUB"), 0)

    def test_distance_between_airports(self):
        reader = FileReader()
        airports = reader.airports
        for Airports, Distance in self.known_values:
            result = TravelPlanner.distance_between_airports(airports.get(Airports[0]), airports.get(Airports[1]))
            self.assertEqual(Distance, result)
            print(Airports, result)

if __name__ == "__main__":
    unittest.main()
