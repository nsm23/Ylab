from heroes import AbstractHero
from places import AbstractPlace
from notifications import AbstractNotifications


class SavePlace:

    def find_villain(self):
        return self.place.get_antagonist()

    def notify(self):
        self.notifier.publication(f'{self.hero.name} saved the {self.place.name}!')

    def __init__(self, hero: AbstractHero, place: AbstractPlace, notifier: AbstractNotifications):
        self.place = place
        self.hero = hero
        self.notifier = notifier

        self.find_villain()
        hero.attack()
        self.notify()

