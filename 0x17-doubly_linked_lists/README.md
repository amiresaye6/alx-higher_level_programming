# Doubly Linked List Implementation in C 📜

A doubly linked list is a linear data structure that consists of nodes where each node has a value and two pointers, one pointing to the previous node and another pointing to the next node. This allows for efficient traversal in both directions. 🔄

## Usage 🚀

### Struct Definition ⚙️

```c
struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
};

struct DoublyLinkedList {
    struct Node* head;
    struct Node* tail;
};
