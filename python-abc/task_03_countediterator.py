

class CountedIterator:
    def __init__(self, item):
        self.nb_item = 0
        self.iterator = iter(item)

    def get_count(self):
        return (self.nb_item)

    def __next__(self):
        try:
            res = next(self.iterator)
            self.nb_item += 1
            return (res)
        except IndexError:
            raise StopIteration
