/** Doubly Linked List */
#include <stdio.h> // required for NULL
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <stdbool.h> // required for bool type

struct node
{
    int key;
    int data;
    struct node *next;
    struct node *prev;
};

struct node *head = NULL;
struct node *tail = NULL;
struct node *curr = NULL;

bool isEmpty()
{
    return head == NULL;
}

int length()
{
    int length = 0;
    struct node *curr;

    for (curr = head; curr != NULL; curr = curr->next)
    {
        length++;
    }
    return length;
}

void displayFoward()
{
    printf("\n[ ");

    struct node *ptr = head; // start at the head
    while (ptr != NULL)
    {
        printf("(%d, %d)", ptr->key, ptr->data);
        ptr = ptr->next;
    }
    printf("");
}

void displayBackward()
{
    printf("\n[ ");

    struct node *ptr = tail; // start at the tail
    while (ptr != NULL)
    {
        printf("(%d, %d) ", ptr->key, ptr->data);

        ptr = ptr->prev;
    }
}

// Insert node at the beginning of the list
void insertFirst(int key, int data)
{
    struct node *node = (struct node *)malloc(sizeof(struct node));
    node->key = key;
    node->data = data;
    // (*node).key = key;
    // (*node).data = data;

    if (isEmpty())
    {
        tail = node;
    }
    else
    {
        head->prev = node;
    }

    // Update pointers and set new head of the list
    node->next = head;
    head = node;
}

// Insert node at the end of the list
void insertLast(int key, int data)
{
    struct node *node = (struct node *)malloc(sizeof(struct node));
    node->key = key;
    node->data = data;

    if (isEmpty())
    {
        // Set the tail node
        tail = node;
    }
    else
    {
        // Update pointers and set new tail node
        tail->next = node;
        node->prev = tail;
    }

    tail = node;
}

struct node *deleteFirst()
{
    // Save reference to former head
    struct node *temp = head;

    // If only one node
    if (head->next == NULL)
    {
        tail = NULL;
    }
    else
    {
        head->next->prev = NULL;
    }

    head = head->next;
    return temp; // return the deleted node
}

struct node *deleteLast()
{
    // save reference to last node
    struct node *temp = tail;

    // if only one link
    if (head->next == NULL)
    {
        head = NULL;
    }
    else
    {
        tail->prev->next = NULL;
    }

    tail = tail->prev;

    return temp;
}

// Delete a node with given key
struct node *delete(int key)
{

    // start from the first link
    struct node *current = head;
    struct node *previous = NULL;

    // if list is empty
    if (head == NULL)
    {
        return NULL;
    }

    // navigate through list
    while (current->key != key)
    {
        // if it is last node

        if (current->next == NULL)
        {
            return NULL;
        }
        else
        {
            // store reference to current link
            previous = current;

            // move to next link
            current = current->next;
        }
    }

    // found a match, update the link
    if (current == head)
    {
        // change first to point to next link
        head = head->next;
    }
    else
    {
        // bypass the current link
        current->prev->next = current->next;
    }

    if (current == tail)
    {
        // change last to point to prev link
        tail = current->prev;
    }
    else
    {
        current->next->prev = current->prev;
    }

    return current;
}

bool insertAfter(int key, int newKey, int data)
{
    // start from the first link
    struct node *current = head;

    // if list is empty
    if (head == NULL)
    {
        return false;
    }

    // navigate through list
    while (current->key != key)
    {

        // if it is last node
        if (current->next == NULL)
        {
            return false;
        }
        else
        {
            // move to next link
            current = current->next;
        }
    }

    // create a link
    struct node *newLink = (struct node *)malloc(sizeof(struct node));
    newLink->key = newKey;
    newLink->data = data;

    if (current == tail)
    {
        newLink->next = NULL;
        tail = newLink;
    }
    else
    {
        newLink->next = current->next;
        current->next->prev = newLink;
    }

    newLink->prev = current;
    current->next = newLink;
    return true;
}

void main()
{
    insertFirst(1, 10);
    insertFirst(2, 20);
    insertFirst(3, 30);
    insertFirst(4, 1);
    insertFirst(5, 40);
    insertFirst(6, 56);

    printf("\nList (First to Last): ");
    displayForward();

    printf("\n");
    printf("\nList (Last to first): ");
    displayBackward();

    printf("\nList , after deleting first record: ");
    deleteFirst();
    displayForward();

    printf("\nList , after deleting last record: ");
    deleteLast();
    displayForward();

    printf("\nList , insert after key(4) : ");
    insertAfter(4, 7, 13);
    displayForward();

    printf("\nList  , after delete key(4) : ");
    delete (4);
    displayForward();
}

// https://www.tutorialspoint.com/data_structures_algorithms/doubly_linked_list_program_in_c.htm
