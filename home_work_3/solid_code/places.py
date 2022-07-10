from abc import ABC, abstractmethod


class AbstractPlace(ABC):

    @property
    def name(self):
        raise NotImplementedError

    @abstractmethod
    def get_antagonist(self):
        ...


class Kostroma(AbstractPlace):
    name = 'Kostroma'

    def get_antagonist(self):
        print('Orcs hid in the forest')


class Tokio(AbstractPlace):
    name = 'Tokio'

    def get_antagonist(self):
        print('Godzilla stands near a skyscraper')


class Titan(AbstractPlace):
    coordinates = [150, 200]

    @property
    def name(self):
        return ','.join(map(str, self.coordinates))

    def get_antagonist(self):
        print('some text, AAAAAAAAAAAA!')
