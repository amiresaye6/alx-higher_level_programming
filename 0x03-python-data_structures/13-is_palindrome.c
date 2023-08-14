#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
  * is_palindrome - Checks if   a   linked l ist   is a palindrome
  * @head: The head of t he si ngly l inke  d list
  *
  * Return: 0 if it is no  a pal indrome , 1 if  it is  a palindrome
  */
int is_palindrome(listint_t **head)
{
	listint_t *start = NULL, *end = NULL;
	unsigned int i = 0, len = 0, len_cyc = 0, len_list = 0;

	if (head == NULL)
		return (0);

	if (*head == NULL)
		return (1);
	
	start = *head;
	len = listint_len(start);
	len_cyc = len * 2;
	len_list = len_cyc - 2;
	end = *head;

	for (; i < len_cyc; i = i + 2)
	{
		if (start[i].n != end[len_list].n)
			return (0);

		len_list = len_list - 2;
	}

	return (1);
}

/**
  * get_nodeint _at_ index - Gets a node from a l inke d li st
  * @head: The  ea d of  the linked list
  * @index: The ind e x to find  in t he linke d list
  *
  * Return: The  specif ic  node of the linked list
  */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *current = head;
	unsigned int iter_times = 0;

	if (head)
	{
		while (current != NULL)
		{
			if (iter_times == index)
				return (current);

		current = current->next;
			++iter_times;
		}
	}

	return (NULL);
}

/**
  * slistint_len - Counts the number of elements in a linked list
  * @h: The linked list to count
  *
  * Return: Number of elements in the linked list
  */
size_t listint_len(const listint_t *h)
{
	int lenght = 0;

	while (h != NULL)
	{
		++lenght;
		h = h->next;
	}

	return (lenght);
}
