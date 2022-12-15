/** Singly Linked List
 */

#include <stdio.h> // required for NULL
// using namespace std;

struct node
{
    int data;
    struct node *next;
};

/* Initialize nodes */
struct node *head;
struct node *one = NULL;
struct node *two = NULL;
struct node *three = NULL;
