""" Doubly Linked List
NODE: [prev|data|next]
Each node stores the data and the address of the next node

HEAD --> [prev|data|next] <-> [prev|data|next] <-> [prev|data|next] -> NULL

Basic Operations:
    prepend(data)       - Adds an element at the beginning of the list.
    append(data)        - Appends an element at the end of the list
    pop_first()         - Deletes an element at the beginning of the list.
    pop_last            - Deletes an element from the end of the list.
    insert_after        - Adds an element after an item of the list.
    delete(data)        - Deletes an element from the list using the key.
    display_forward()   - Displays the complete list in a forward manner.
    display_backward()  - Displays the complete list in a backward manner.
"""


class Node(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self) -> str:
        # return "Node(data={self.data}, prev={self..data}, next={self.next.data})"
        return print(f"Node({self.data})")


class DLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # def __repr__(self):
    #     curr = self.head
    #     nodes = "\n"
    #     while curr is not None:
    #         nodes += repr(curr) + " --> "
    #         curr = curr.next
    #     nodes += "None\n"
    #     return nodes

    def __repr__(self) -> str:
        curr = self.head
        nodes = []
        while curr is not None:
            nodes.append("[" + str(curr.data) + "]")
            curr = curr.next
        nodes.append("None")
        return " --> ".join(nodes)

    def __str__(self):
        """Prints the node data from the list"""
        nodes = []
        llist = "["
        curr = self.head
        while curr and curr.next is not None:
            nodes.append(curr.data)
            curr = curr.next
        # return ", ".join(map(str, nodes))
        llist += "] --> [".join(map(str, nodes)) + "]"
        return llist

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
        # return (self.head is None) ? True: False
        # return True if self.head is None else False

    def fetch_tail(self):
        """Returns the last node in the list"""
        curr = self.head
        while curr and curr.next is not None:
            curr = curr.next
        return curr

    def append(self, data):
        """Appends new node to end of list"""
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            tail = self.fetch_tail()  # current last
            tail.next = node
            self.tail = node
            self.tail.prev = tail
            self.tail.next = None
        self.count += 1

    def prepend(self, data):
        """Adds node to beginning of list"""
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            node.prev = None
            node.next = self.head
            self.head = node
        self.count += 1

    def pop_first(self):
        """Removes the first node from the list.
           Returns the data of the last node removed."""
        if not self.is_empty():
            temp = self.head
            self.head = self.head.next
            self.count -= 1
            print(f"\nNode({temp.data}) was removed from the list")
            return temp.data  # returns the last data removed
        return None

    def pop_last(self):
        """Removes the last node from the list.
           Returns the data of the last node removed."""
        if not self.is_empty():
            prev = None
            curr = self.head
            while curr and curr.next is not None:
                prev = curr
                curr = curr.next
            prev.next = None
            self.tail = prev
            self.count -= 1
            print(f"\nNode({curr.data}) was removed from the list")
            return curr.data  # returns the last data removed
        return None

    def insert_after(self, item, data):
        """Adds an new node after an node:item of the list."""
        prev = None
        curr = self.head
        while curr and curr.next is not None:
            prev = curr
            curr = curr.next
            if (prev.next.data == item.data and curr.data == item.data):
                # node = Node(data)
                # node.prev = prev
                # node.next = curr
                node = Node(data, prev=prev, next=curr)
                prev.next = node
                curr.prev = node
                self.count += 1
                print(f"\nNode({data}) was inserted after Node({item.data})")
                return True
        print(f"\nNode({item}) not found in list")
        return False

    def remove(self, item):
        """Removes a node:item from the list using the key:data.
           Returns True if the node was removed"""
        prev = None
        curr = self.head
        while curr and curr.next is not None:
            prev = curr
            curr = curr.next
            if (curr.data == item.data):
                prev.next = curr.next
                curr.next.prev = prev
                self.count -= 1
                print(f"\nNode({item.data}) was removed")
                return True
        print(f"\nNode({item.data}) could not be removed")
        return False

    def display(self, reverse=False):
        nodes = ["HEAD"]
        curr = self.head
        while curr is not None:
            nodes.append(curr.data)
            curr = curr.next
        nodes.append("NONE")
        if reverse:
            nodes.reverse()
        return " --> ".join(map(str, nodes))

    # def display_forward(self):
    #     """Displays the complete list in a foward manner"""
    #     nodes = ["HEAD"]
    #     curr = self.head
    #     while curr is not None:
    #         nodes.append(curr.data)
    #         curr = curr.next
    #     nodes.append("NONE")
    #     return " --> ".join(map(str, nodes))

    # def display_backward(self):
    #     """Displays the complete list in a backward manner"""
    #     nodes = ["HEAD"]
    #     curr = self.head
    #     while curr is not None:
    #         nodes.append(curr.data)
    #         curr = curr.next
    #     nodes.append("NONE")
    #     nodes.reverse()
    #     return " --> ".join(map(str, nodes))


if __name__ == "__main__":
    llist = DLinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.prepend(0)
    llist.append(4)
    llist.prepend(-1)
    # print(llist.display_forward())
    # print(llist.display_backward())
    print(llist.display())
    print(llist.display(reverse=True))
    llist.remove(Node(-100))
    print(llist.display())

    llist.remove(Node(0))
    print(llist.display())

    llist.insert_after(Node(2), 100)
    print(llist.display())

    llist.pop_first()
    print(llist.display())

    llist.pop_last()
    print(llist.display())

    print(repr(llist))
    print(str(llist))


# map(function, iterable) : maps a function to each item in the iterable
# delimter.join(iterable) : joins every item in the iterable into a single delimited string
