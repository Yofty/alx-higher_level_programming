#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * list : is the linked list to be checked
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *x;

	if (list == NULL)
		return (0);
	x = list->next;

	while (x != NULL)
	{
		if (x == list)
			return (1);
		x = x->next;
	}
	return (0);
}
