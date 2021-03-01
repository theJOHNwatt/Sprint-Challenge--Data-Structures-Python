from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()


    def append(self, item):
        if self.current is None:
            self.current = self.storage.head 

        if self.storage.length >= self.capacity: 
            if self.current == self.storage.head:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.current.next 
            elif self.current == self.storage.tail:
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
                self.current = self.storage.head 
            else: 
                self.current.insert_before(item)
                temp = self.current.next 
                self.storage.delete(self.current)
                self.current = temp
                self.storage.length += 1 
        else:
            self.storage.add_to_tail(item)
        


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current_node = self.storage.head

        # TODO: Your code here
        while current_node is not None: 
            current_value = current_node.value 
            list_buffer_contents.append(current_value)
            current_node = current_node.next

        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
