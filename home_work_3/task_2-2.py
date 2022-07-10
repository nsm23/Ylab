from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


"""Дан class Movie. 
Реализуйте у него метод schedule. 
Он будет генерировать дни, в которые показывают фильм."""


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        step = timedelta(days=1)
        for date in self.dates:
            start: datetime = date[0]
            while start <= date[1]:
                yield start
                start += step


m = Movie('sw',
          [
              (datetime(2020, 1, 1), datetime(2020, 1, 7)),
              (datetime(2020, 1, 15), datetime(2020, 2, 7)),
              (datetime(2022, 6, 10), datetime(2022, 6, 15)),
          ])

for d in m.schedule():
    print(d)
