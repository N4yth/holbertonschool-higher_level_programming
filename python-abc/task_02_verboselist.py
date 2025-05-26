

class VerboseList(list):
    def append(self, item):
        super(VerboseList, self).append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        super(VerboseList, self).extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        super(VerboseList, self).remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, item=None):
        if item is None:
            item = len(self) - 1
        resu = super(VerboseList, self).pop(item)
        print("Popped [{}] from the list.".format(resu))
