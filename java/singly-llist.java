// package DataStructures.Java;
// public class singly-llist {
// }asd

class LinkedList {
    Node head;

    static class Node {
        int data;
        Node next;

        Node(int d) {
            data = d;
            next = null;
        }
    }

    public static void main(String[] args) {
        LinkedList linkedlist = new LinkedList();

        // Assign values
        linkedlist.head = new Node(1);
        Node second = new Node(2);
        Node third = new Node(3);

        // Connect the nodes
        linkedlist.head.next = second;
        second.next = third;

        // Printing nodes
        while (linkedlist.head != null) {
            System.out.print(linkedlist.head.data + " ");
            linkedlist.head = linkedlist.head.next;
        }

    }
}
