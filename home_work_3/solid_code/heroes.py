from abc import ABC, abstractmethod
from weapons import KarateMixin, SuperMixin, GunMixin


class AbstractHero(ABC):
    @property
    def name(self):
        raise NotImplementedError

    @abstractmethod
    def attack(self):
        ...


class SuperHero(AbstractHero):
    def ultimate(self):
        ...


class SuperMan(KarateMixin, SuperMixin, SuperHero):
    name = 'Clark Kent'

    def attack(self):
        self.roundhouse_kick()
        self.ultimate()

    def ultimate(self):
        self.incinerate_with_lasers()


class ChuckNorris(KarateMixin, GunMixin, AbstractHero):
    name = 'Chuck Norris'

    def attack(self):
        self.roundhouse_kick()
        self.fire_a_gun()
