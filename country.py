class Country(object):

    def __init__(self, name, currency):
        self._name = name
        self._currency = currency

    @property
    def name(self):
        return self._name

    @property
    def currency(self):
        return self._currency
