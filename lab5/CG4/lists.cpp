#include "lists.h"
#include <QDebug>
void add_active_edge(node_t** head, Edge_active& edge)
{
    node_t* new_edge = (node_t*)malloc(sizeof(node_t));

    if (new_edge != NULL)
    {
        new_edge->next = *head;
        new_edge->edge = edge;
        *head = new_edge;
    }
}


Edge_active pop_active_edge(node_t** head)
{
    Edge_active edge = (*head)->edge;
    node_t* deletion;
    deletion = *head;
    *head = (*head)->next;
    free(deletion);

    return edge;
}

void free_list(node_t** head)
{
    while (*head)
    {
        node_t* deletion;
        deletion = *head;
        *head = (*head)->next;
        free(deletion);
    }
    //free(*head);
}

void free_x_list(list** head)
{
    while (*head)
    {
        list* deletion;
        deletion = *head;
        *head = (*head)->next;
        free(deletion);
    }
    //free(*head);
}

void add_active_edges(node_t** y_group, node_t** active_edges_list)
{
    node_t* temp = *y_group;
    while (*y_group)
    {
        //Edge_active edge = pop_active_edge(y_group);
        Edge_active edge = (*y_group)->edge;
        add_active_edge(active_edges_list, edge);
        *y_group = (*y_group)->next;
    }
    *y_group = temp;
}


int has_adjacent_edge(node_t** string, Edge_active &edge)
{
    int check = 0;
    node_t* temp = *string;
    while (*string && check != 2)
    {
        if ((*string)->edge.x == edge.x)
            check++;
    }
    *string = temp;

    if (check != 2)
        check = 0;
    return  check;
}

///совпадение координаты х у ребра и у одного из ребер след строки
int is_crossing_in_extremum_vertex(node_t** next_string, node_t** active_edges_list)
{

    int check = 1;
    /*
    node_t* temp = *next_string;
    while (*next_string && !check)
    {
        if ((*active_edges_list)->edge.x == (*next_string)->edge.x)
            check = 1;

        *next_string = (*next_string)->next;
    }
    *next_string = temp;
    */
    if ((*active_edges_list)->edge.y - 1 == 1 && has_adjacent_edge(next_string, (*active_edges_list)->edge))
        check = 1;




    /*
    int check = 0;
    node_t* temp = *next_string;
    while ((*next_string)->next && (*active_edges_list)->next)
    {
        if ((*active_edges_list)->edge.x == (*active_edges_list)->next->edge.x)
            check = 1;

        *next_string = (*next_string)->next;
    }
    *next_string = temp;
    */
    return check;
}



void del_unactive_edges(node_t** next_string, node_t** active_edges_list)
{
    node_t* temp = *active_edges_list;
    node_t* prev = NULL;
    int deleted = 0;
    while (*active_edges_list)
    {
        deleted = 0;
        if ((*active_edges_list)->edge.dy - 1 == 0)
        {
            if ((*active_edges_list) != temp)
            {
                pop_active_edge(active_edges_list);
                prev->next = *active_edges_list;
            }
            else
            {
                pop_active_edge(active_edges_list);
                temp = *active_edges_list;
            }
            deleted = 1;
        }       
        else if (!is_crossing_in_extremum_vertex(next_string, active_edges_list))
        {
            if ((*active_edges_list) != temp)
            {
                pop_active_edge(active_edges_list);
                prev->next = *active_edges_list;
            }
            else
            {
                pop_active_edge(active_edges_list);
                temp = *active_edges_list;
            }
            deleted = 1;
        }
        prev = *active_edges_list;
        if (!deleted && *active_edges_list)
            *active_edges_list = (*active_edges_list)->next;
    }
    *active_edges_list = temp;
}


void preparation_active_edges(node_t** active_edges_list)
{
    node_t* temp = *active_edges_list;
    while (*active_edges_list)
    {
        (*active_edges_list)->edge.dy -= 1;
        (*active_edges_list)->edge.x += (*active_edges_list)->edge.dx;
        *active_edges_list = (*active_edges_list)->next;
    }
    *active_edges_list = temp;
}




void add_x_to_list(list** head, double x)
{
    list* new_list = (list*)malloc(sizeof(list));

    if (new_list != NULL)
    {
        new_list->next = *head;
        new_list->x = x;
        *head = new_list;
    }
}


int fill_x_list(node_t* active_edges_list, list** x_list)
{
    int amount = 0;
    node_t* temp = active_edges_list;
    while (active_edges_list)
    {
        //Edge_active edge = pop_active_edge(active_edges_list);
        Edge_active edge = (active_edges_list)->edge;
        add_x_to_list(x_list, edge.x);

        active_edges_list = (active_edges_list)->next;
        amount++;
     }
     active_edges_list = temp;

     return amount;
}


void sort_x_list(list** head)
{
    list* start = *head;
    qDebug() << "DIO";
    while((*head)->next)
    {
        list* temp = *head;
        while((*head)->next)
        {
            if ((*head)->x > (*head)->next->x)
            {
                double swap = (*head)->x;
                (*head)->x = (*head)->next->x;
                (*head)->next->x = swap;
            }
            *head = (*head)->next;
        }
        *head = temp;
        *head = (*head)->next;
    }
    *head = start;
}


void sort(list **root)
{
    list *p, *key;
    list *result = *root;
    qDebug() << "DI";
    *root = (*root)->next;      /* Головой стал следующий элемент */
    result->next = NULL;    /* Первый элемент отсортированного списка */

    qDebug() << "DIO";
    while((*root)->next != NULL)
    {
        key = *root;
        *root = (*root)->next;
        if(key->x < result->x)
        {   /* Вставляем результат в голову */
            key->next = result;
            result = key;
        }
        else
        {
            p = result;
            while(p->next != NULL)
            {     /* Бежим по уже сформированному результату */
                if(p->next->x > key->x)
                    break;
                p = p->next;
            }
            key->next = p->next;
            p->next = key;
        }
    }
    *root = result;
}


void insertion_sort(list **head_ref)

{
    if (*head_ref)
    {
       // Инициализируем отсортированный связанный список
        list *sorted = NULL;
        // Переходим по указанному связанному списку и вставляем каждый
        // узел отсортирован
        list *current = *head_ref;

        while (current != NULL)
        {
            list *next = current->next;
            sorted_insert(&sorted, current);
            // Обновить текущий
            current = next;
        }
        // Обновляем head_ref, чтобы он указывал на отсортированный связанный список
       *head_ref = sorted;
    }
}


void sorted_insert(list** head_ref, list* new_node)

{
    list* current;

    if (*head_ref == NULL || (*head_ref)->x >= new_node->x)
    {
        new_node->next = *head_ref;
        *head_ref = new_node;
    }
    else
    {
        current = *head_ref;

        while (current->next!=NULL && current->next->x < new_node->x)
            current = current->next;

        new_node->next = current->next;
        current->next = new_node;

    }

}


void print_list(list* head)
{
    list* temp = head;
    while (head)
    {
        qDebug() << (head)->x;
        head = (head)->next;
    }
    head = temp;
    qDebug() <<  "______________";
}
/*
void sort_list(node_t** head)
{
    node_t* start = *head;

    while (*head)
    {
        node_t* temp = *head;
        while (*head)
        {
            if ((*head)->edge.x > (*head)->next->edge.x)
            {
                double swap = (*head)->edge.x;
                (*head)->edge.x = (*head)->next->edge.x;
                (*head)->next->edge.x = swap;
            }
            *head = (*head)-> next;
        }
        *head = temp;
        *head = (*head)-> next;
    }
    *head = start;
}
*/
