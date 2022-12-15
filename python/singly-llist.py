""" Singly Linked List

NODE: [data|next]
Each node stores the data and the address of the next node

HEAD --> [data|next] -> [data|next] -> [data|next] -> NULL

Basic Operations:
    prepend(data)   - Add a node in the beginning
    append(data)    - Add a node in the end
    pop_last()      - Remove a node from the end
    pop_first()     - Remove a node from the beginning
    head()          - Return the first node
    tail()          - Return the last node
    remove(Node)    - Remove Node from the list
"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    # def __repr__(self) -> str:
    #     return "Node=%d" % self.data # str(self.data)

    def __repr__(self) -> str:
        return f"Node({self.data})"

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next


class SLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # def __repr__(self) -> str:
    #     node = self.head
    #     nodes = []
    #     while node is not None:
    #         nodes.append("[" + str(node.data) + "]")
    #         node = node.next
    #     nodes.append("None")
    #     return " --> ".join(nodes)

    def __repr__(self):
        node = self.head
        nodes = "\n"
        while node is not None:
            nodes += repr(node) + " --> "
            node = node.next
        nodes += "None\n"
        return nodes

    def __str__(self):
        """Prints the node data from the list"""
        values = []
        nodes = "["
        curr = self.head
        while curr and curr.next is not None:
            values.append(curr.data)
            curr = curr.next
        nodes += "] --> [".join(map(str, values)) + "]"
        return nodes

    def set_head(self, head):
        self.head = head

    def get_head(self):
        return self.head

    def is_empty(self):
        if self.head is None:
            return True
        else:
            False

    # def count(self):
    #     """Counts the number of items in the list"""
    #     count = 0
    #     curr = self.head
    #     while curr and curr.next is not None:
    #         count += 1
    #     print(f"Total Nodes: {self.count}\n")
    #     return count

    def get_count(self):
        return self.count

    def get_tail(self):
        """Traverses to end and returns the last node in the list"""
        curr = self.head
        while curr and curr.next is not None:
            curr = curr.next
        return curr  # last node

    def append(self, data):
        "Add node to end of list"
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.head.next = None
        else:
            tail = self.get_tail()
            tail.next = node
            self.tail = node   # node  # curr
            self.tail.next = None
        self.count += 1
        # print(f"Last Node: {self.tail}")
        # print(f"Total Node: {self.count}")

    def prepend(self, data):
        """Adds node to beginning of list"""
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.count += 1

    def pop_last(self):
        """Remove a node from the end of list"""
        if self.is_empty():
            return None
        else:
            prev = None
            curr = self.head
            while curr.next is not None:
                prev = curr
                curr = curr.next
            prev.next = None
            self.count -= 1
        # print(f"Last Node: {self.tail}")
        # print(f"Total Node: {self.count}")

    def pop_first(self):
        """Remove a node from the beginning of the list"""
        self.head = self.head.next
        self.count -= 1

    def head(self):
        # return repr(Node(self.head))
        # return Node.__repr__(self.head)
        return self.head

    def tail(self):
        # tail = self.get_tail(self.head)
        # print("last: " + str(tail.data))
        # return tail
        return self.tail

    def remove(self, node):
        """Removes a Node from the list"""
        if self.is_empty():
            return None
        else:
            prev = None
            curr = self.head
            while curr and curr.next is not None:
                prev = curr
                curr = curr.next
                if node.data == curr.data:
                    prev.next = curr.next
                    self.count -= 1
                    break


if __name__ == '__main__':
    one = Node(1)
    print(repr(one))
    llist = SLinkedList()
    llist.append(0)
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.prepend(-1)
    llist.prepend(-2)
    print(repr(llist))
    print(str(llist))
    llist.pop_first()
    print(repr(llist))
    llist.pop_last()
    print(repr(llist))

    llist.remove(Node(3))
    print(repr(llist))

    llist.remove(Node(-3))
    print(repr(llist))

    llist.remove(Node(-8))
    print(repr(llist))
    # print(repr(llist.head))
    # print(repr(llist.tail))
    # print(repr(llist.head()))
    # print(repr(llist.tail()))
    # print(repr(str(llist.head)))
    # repr(llist)

    # print(repr(llist.get_tail()))
    # print(repr(fetch_last(llist)))
    # print(repr(fetch_last(llist.head)))


# https://lucasmagnum.medium.com/sidenotes-linked-list-abstract-data-type-and-data-structure-fd2f8276ab53
