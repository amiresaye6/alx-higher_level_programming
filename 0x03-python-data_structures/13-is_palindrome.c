#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of head of list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *second_half;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}

	second_half = slow;
	prev->next = NULL;
	second_half = reverse_list(&second_half);

	while (second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
			return (0);
		}
		*head = (*head)->next;
		second_half = second_half->next;
	}
	return (1);
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to pointer of head of list
 * Return: pointer to new head of reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}
