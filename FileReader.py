import csv, os

from Airport import Airport
from Currency import Currency, ExchangeRate
from Aircraft import Aircraft


class FileReader:
    airports = {}
    currencies = {}
    aircraft = {}
    rates = {}

    def __init__(self):
        self.load_airports("CSV/Airports.csv")
        self.load_currencies("CSV/NationalCurrencies.csv")
        self.load_conversion_rates("CSV/CurrencyExchangeRates.csv")
        self.load_aircraft("CSV/Aircraft.csv")

    def load_airports(self, filename):
        with open(os.path.join(filename), "rt", encoding="utf8") as f:
            reader = csv.reader(f)
            for line in reader:
                try:
                    self.airports[line[4]] = Airport(line[4], line[1], line[3], line[2], line[6], line[7])
                except KeyError:
                    continue

    def load_currencies(self, filename):
        with open(os.path.join(filename), "rt", encoding="utf8") as f:
            reader = csv.reader(f)
            for line in reader:
                try:
                    self.currencies[line[0].upper()] = Currency(line[17], line[14], line[0].upper())
                except KeyError:
                        continue

    def load_aircraft(self, filename):
        with open(os.path.join(filename), "rt", encoding="utf8") as File:
            reader = csv.reader(File)
            for line in reader:
                try:
                    self.aircraft[line[0]] = Aircraft(line[0], line[1], line[2], line[3], int(line[4]))
                except KeyError:
                        continue

    def load_conversion_rates(self, filename):
        with open(os.path.join(filename), "rt", encoding="utf8") as File:
            ExchangeLine = csv.reader(File)
            for line in ExchangeLine:
                try:
                    self.rates[line[1]] = ExchangeRate(line[1], line[0], line[2], line[3])
                except KeyError:
                    continue


