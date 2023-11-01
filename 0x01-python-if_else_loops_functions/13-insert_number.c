#include "lists.h"
#include <stdlib.h>

/**
* insert_node - Inserts the number into the sorted singly-linked list
* @head: It a pointer to the head of a linked list
* @number: It the number to be inserted.
* Return: returns 0 if the function failed or the pointer to the new node.
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *newest;


	newest = malloc(sizeof(listint_t));
	if (newest == NULL)
	return (NULL);

	newest->n = number;

	if (node == NULL || node->n >= number)
	{
	newest->next = node;
	*head = newest;
	return (newest);
	}

	while (node && node->next && node->next->n < number)
	{
	node = node->next;
	}

	newest->next = node->next;
	node->next = newest;

	return (newest);
}
