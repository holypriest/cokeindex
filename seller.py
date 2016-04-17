from country import Country

class Seller(object):

    def __init__(self, name, country):
        self._name = name
        self._country = country

    @property
    def name(self):
        return self._name

    @property
    def country(self):
        return self._country
