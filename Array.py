class Array:


    def __init__(self, capacity):
        self._items = []
        self.logical_size = 0

        for i in range(capacity):
            self._items.append(None)


    def get_logical_size(self):
        return self.logical_size


    def __len__(self):
        return len(self._items)


    def __str__(self):
        return str(self._items)


    def __iter__(self):
        return iter(self._items)


    def __getitem__(self, index):
        return self._items[index]


    def __setitem__(self, index, new_item):

        if not new_item:

            if (self.logical_size != index + 1):
                raise Exception('Cannot update index, before the last logically filled index of the array, to null')
            else:
                new_logical_size = self.logical_size - 1
        
        else:

            if (index != self.logical_size):
                raise Exception("Cannot update index, further than the first logically empty index of the array")
            else:
                new_logical_size = self.logical_size + 1
		
        try:
            self._items[index] = new_item
            self.logical_size = new_logical_size

        except IndexError:
            raise IndexError("Array does not have an index " + str(index))


    def __eq__(self, other):

        if self is other:
            return True
        
        if type(self) != type(other):
            return False
        
        if self.logical_size != other.logical_size:
            return False
        
        for i in range(self.logical_size):
            if self._items[i] != other._items[i]:
                return False
        
        return True