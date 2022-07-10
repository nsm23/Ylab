"""
Написать класс CyclicIterator.
Итератор должен итерироваться по итерируемому объекту
(list, tuple, set, range, Range2, и т. д.), и когда
достигнет последнего элемента, начинать сначала.
"""


class CyclicIterator:
    def __init__(self, container):
        self.container = container
        self.iter = iter(container)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iter)
        except StopIteration:
            self.iter = iter(self.container)
            return next(self.iter)


cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)
