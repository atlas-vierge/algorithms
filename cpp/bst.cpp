// Binary Search Tree in C++
#include<iostream>
using namespace std;

struct BSTNode {
    int data;
    BSTNode *left;
    BSTNode *right;
};


void Insert(BSTNode** rootPtr, int data) {
    if (*rootPtr == NULL) { // empty tree
        *rootPtr = GetNewNode(data);
        return rootPtr;
    }
}


BSTNode* Insert(BSTNode* root, int data) {
    if (root == NULL) { // empty tree
        root = GetNewNode(data);
        return root;
    }
}


BSTNode* GetNewNode(int data) {
    // BSTNode* newNode = (BSTNode*)malloc(sizeof(BSTNode)); // C
    BSTNode *newNode = new BSTNode(); // C++
    // (*newNode).data = data;
    newNode->data = data;
    // newNode->left = NULL; newode->right = NULL;
    newNode->left = NULL;
    newode->right = NULL;
    return newNode;
}


int main() {
    BSTNode *root = NULL;
    // Insert(&root, 15);
    // Insert(&root, 20);
    // Insert(&root, 25);
    root = Insert(root, 15);
    root = Insert(root, 20);
    root = Insert(root, 25);
}
