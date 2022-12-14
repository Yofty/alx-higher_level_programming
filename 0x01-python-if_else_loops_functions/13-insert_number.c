#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head : is the head of the link
 * @number : is the number to be added
 * Return: x
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *x, *c;

	c = *head;

	x = malloc(sizeof(listint_t));
	if (x == NULL)
		return (NULL);

	x->n = number;
	x->next = NULL;

	if (*head == NULL)
		*head = x;
	else
	{
		while (c->next != NULL)
		{
			c = c->next;
		}
		c->next = x;
	}
	return (x);
}
