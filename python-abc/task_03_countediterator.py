

class CountedIterator:
    def __init__(self, item):
        self.nb_item = 0
        self.iterator = iter(item)

    def get_count(self):
        return (self.nb_item + 1)

    def __next__(self):
        self.nb_item += 1
        try:
            return (next(self.iterator))
        except IndexError:
            raise StopIteration
