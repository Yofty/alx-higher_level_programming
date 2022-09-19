#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * list : is the linked list to be checked
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *x, *y;

	if (list == NULL)
		return (0);
	y = list;
	x = list->next;

	while (x && y && x->next)
	{
		if (x == y)
			return (1);
		y = y->next;
		x = x->next->next;
	}
	return (0);
}
