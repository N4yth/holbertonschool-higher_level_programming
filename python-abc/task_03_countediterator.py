

class CountedIterator:
    def __init__(self, iter, nb_item=-1):
        self.nb_item = nb_item
        self.iter = iter

    def get_count(self):
        return (self.nb_item + 1)

    def __next__(self):
        self.nb_item += 1
        try:
            return (self.iter[self.nb_item])
        except IndexError:
            raise StopIteration
