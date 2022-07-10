from abc import ABC, abstractmethod


class AbstractNotifications(ABC):
    @abstractmethod
    def publication(self, text):
        ...


class NewsPaperNotifications(AbstractNotifications):
    def publication(self, text):
        print(f'BBC news today: {text}')


class TvNotifications(AbstractNotifications):
    def publication(self, text):
        print(f'RenTv today, {text}')

