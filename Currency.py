class Currency:

    def __init__(self, name, code, country):
        self.name = name
        self.code = code
        self.country = country

    def get_code(self):
        return self.code

    def __str__(self):
        return "Code: {}, Name: {}, Country: {},".format(self.code, self.name, self.country,)


class ExchangeRate:
    def __init__(self, name, code, in_euro, from_euro):
        self.name = name
        self.code = code
        self.in_euro = float(in_euro)
        self.from_euro = float(from_euro)

    def __str__(self):
        return "{}(Currency Name:{}, In Euro:{}, From Euro:{})".format(self.name, self.code,
                                                                       self.in_euro, self.from_euro)
