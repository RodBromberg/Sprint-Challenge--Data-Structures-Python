from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            if self.storage.length == self.capacity:
                old_head = self.storage.head
                self.storage.remove_from_head()
                self.storage.add_to_tail(item)
            if old_head == self.current:
                self.current = self.storage.tail

    def get(self):
        list_buffer_contents = []
        current = self.storage.head
        while current:
            list_buffer_contents.append(current.value)
            current = current.next
        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
