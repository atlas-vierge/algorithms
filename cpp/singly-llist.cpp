// #include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
};

int main()
{
    Node *head;
    Node *one = NULL;
    Node *two = NULL;
    Node *three = NULL;

    // Allocate 3 nodes in the heap
    one = new Node();
    two = new Node();
    three = new Node();

    // Assign values to data
    one->data = 1;
    two->data = 2;
    three->data = 3;

    // Connect the nodes
    one->next = two;
    two->next = three;
    three->next = NULL;

    // Print the Linked list value
    head = one;
    while (head != NULL)
    {
        cout << head->data;
        head = head->next;
    }
}
