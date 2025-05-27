#!/usr/bin/env python3

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        if item in self:
            print("Removed [{}] from the list.".format(item))
            super().remove(item)
        else:
            raise ValueError("list.remove(x): x not in list")

    def pop(self, item=None):
        if item is None:
            item = len(self) - 1
        try:
            print("Popped [{}] from the list.".format(self[item]))
            resu = super().pop(item)
        except IndexError:
            raise IndexError("pop index out of range")
