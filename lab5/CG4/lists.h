#ifndef LIST_H
#define LIST_H
#include "edge.h"
#include <iostream>
#include <list>

struct node_t
{
    Edge_active edge;
    struct node_t* next;
};


struct list
{
    double x;
    struct list* next;
};


struct list_x
{
    int amount;
    struct list;
};

void add_active_edge(node_t** head, Edge_active& edge);
void add_active_edges(node_t** y_group, node_t** active_edges_list);
Edge_active pop_active_edge(node_t** head);
int is_crossing_in_extremum_vertex(node_t** next_string, node_t** active_edges_list);
void del_unactive_edges(node_t** next_string, node_t** active_edges_list);
void preparation_active_edges(node_t** active_edges_list);
void free_list(node_t** head);
void free_x_list(list** head);
void sort_list(node_t** head);

void add_x_to_list(list** head, double x);
int fill_x_list(node_t* active_edges_list, list** x_list);
void sort_x_list(list** head);
void sort(list** root);

void sorted_insert(list** head_ref, list* new_node);
void insertion_sort(list **head_ref);

void print_list(list* head);

int has_adjacent_edge(node_t** string, Edge_active &edge);
#endif // LIST_H
