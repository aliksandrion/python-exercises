from abc import ABC, abstractmethod


class Place(ABC):

    @abstractmethod
    def get_local_antagonist(self):
        pass


class Kostroma(Place):
    name = 'Kostroma'

    def get_local_antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    name = 'Tokyo'

    def get_local_antagonist(self):
        print('Godzilla stands near a skyscraper')
