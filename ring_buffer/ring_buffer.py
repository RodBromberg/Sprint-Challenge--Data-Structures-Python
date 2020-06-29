from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):

        self.capacity = capacity
        self.storage = []
        self.current_item = 0

    def append(self, item):
        # [1] item = 1
        # [1,2] item = 2
        # [1,2,3] item = 3
        # [4,2,3] item = 4 at capacity
        # [4,5,3] item = 5 at capacity
        # [4,5,6]
        # if length of array is NOT greater than capacity push item to arr
        # otherwise overwrite the storage[current_item] index to the new item
        # return storage
        # increment the index by 1 until it reaches capacity then reset to 0
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            return self.storage

        else:
            self.storage[self.current_item] = item
            self.current_item += 1

        if self.current_item == self.capacity:
            self.current_item = 0

    def get(self):
        return self.storage


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
