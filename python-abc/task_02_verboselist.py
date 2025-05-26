

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        try:
            super().remove(item)
        except ValueError:
            raise ValueError

    def pop(self, item=None):
        if item is None:
            item = len(self) - 1
        print("Popped [{}] from the list.".format(self[item]))
        resu = super().pop(item)
