#include "lists.h"
/**
 * reverse_listint - reverses the linked list
 * @head: points the first node at the list
 * Return: pointer at the first node at new list
 */
void reverse_the_listint(listint_t **thehead)
{
	listint_t *prev = NULL;
	listint_t *current = *thehead;
	listint_t *next = NULL;
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*thehead = prev;
}

/**
 * is_palindrome - checks if the linked list is the palindrome
 * @head: double pointer at the linked list
 *
 * Return: return 1 if it is, returns 0 if not
 */

int is_palindrome(listint_t **thehead)
{
	listint_t *slow = *thehead, *fast = *thehead, *temp = *thehead, *d = NULL;

	if (*thehead == NULL || (*thehead)->next == NULL)
		return (1);
	while (1)
	{
        fast = fast->next->next;
		if (!fast)
		{
			d = slow->next;
			break;
		}
        if (!fast->next)
		{
			d = slow->next->next;
			break;
		}
		slow = slow->next;
    }

    reverse_the_listint(&d);
    while (d && temp)
	{
		if (temp->n == d->n)
		{
			d = d->next;
			temp = temp->next;
		}

        else
			return (0);
        }

	if (!d)
		return (1);
    
    return (0);
}