/** Doubly Linked List in C
 */

#include <stdio.h>

struct node
{
    node *next;
    node *prev;
    // ...
};

struct list
{
    node *head = nullptr;
    node *tail = nullptr;
};

/** Insert node:n at the beginning of list:l */
// void list_push_front(list *list, node *node)
// {
//     node->next = list->head;
//     node->prev = nullptr;
//     if (list->head)
//     {
//         list->head->prev = node;
//     }
//     list->head = node;
// }
void list_push_front(list *l, node *n)
{
    n->next = l->head;
    n->prev = nullptr;
    if (l->head)
    {
        l->head->prev = n;
    }
    else
    {
        l->tail = n;
    }
    l->head = n;
}

void list_push_back(list *l, node *n)
{
    n->next = nullptr;
    n->prev = l->tail;
    if (l->tail)
    {
        l->tail->next = n;
    }
    else
    {
        l->head = n;
    }
    l->tail = n;
}

/** Remove `n` from `l`. */
// void list_erase(list *l, node *n)
// {
//     if (n->next)
//     {
//         n->next->prev = n->prev;
//     }
//     if (n->prev)
//     {
//         n->prev->next = n->next;
//     }
//     else
//     {
//         l->head = n->next;
//     }
// }
void list_erase(list *l, node *n)
{
    if (n->next)
    {
        n->next->prev = n->prev;
    }
    else
    {
        l->tail = n->prev;
    }
    if (n->prev)
    {
        n->prev->next = n->next;
    }
    else
    {
        l->head = n->next;
    }
}

/** Remove node:n from list:l */
void list_remove_node(list *list, node *node)
{
    if (node->next)
    {
        node->next->prev = node->prev;
    }

    if (node->prev) // prev node is not HEAD
    {
        node->prev->next = node->next;
    }
    else // prev node is HEAD node
    {
        list->head = node->next;
    }
}

// https://cs61.seas.harvard.edu/site/2022/Patterns/#gsc.tab=0
