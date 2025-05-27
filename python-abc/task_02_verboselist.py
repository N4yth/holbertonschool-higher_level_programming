#!/usr/bin/env python3

class VerboseList(list):
    def append(self, item):
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, item):
        print("Extended the list with [{}] items.".format(len(item)))
        super().extend(item)

    def remove(self, item):
        if item in self:
            print("Removed [{}] from the list.".format(item))
            super().remove(item)

    def pop(self, item = -1):
        resu = super().pop(item)
        print("Popped [{}] from the list.".format(resu))
        return resu
