#!/usr/bin/env python3
""" Shapes, Interfaces, and Duck Typing
"""


class VerboseList(list):
    """
    A subclass of the built-in list class that
    provides additional verbosity for list operations.

    Methods:
    - append(item): Appends an item to the list and prints
    a message indicating the item that was added.
    - extend(item): Extends the list with the items from
    another iterable and prints a message indicating the number of items added.
    - remove(item): Removes the first occurrence of an item from
    the list and prints a message indicating the item that was removed.
    - pop(index=None): Removes and returns the item at the specified index
    (default is the last item) and prints
    a message indicating the item that was popped.
    """

    def append(self, item):
        """
        Appends an item to the list and prints a message
        indicating the item that was added.

        Args:
            item: The item to be added to the list.
        """
        super().append(item)
        print("Added [{}] to the list".format(item))

    def extend(self, item):
        """
        Extends the list with the elements from the given iterable.

        Args:
            item (iterable): The iterable containing the elements
            to be added to the list.

        Returns:
            None
        """
        super().extend(item)
        print("Extended the list with [{}] items".format(len(item)))

    def remove(self, item):
        """
        Removes an item from the list.

        Args:
            item: The item to be removed from the list.

        Returns:
            None
        """
        print("Removed [{}] from the list".format(item))
        super().remove(item)

    def pop(self, index=None):
        """
        Remove and return an element from the list.

        Args:
            index (int, optional): The index of the element to be removed.
            If not specified, the last element is removed.

        Returns:
            The removed element.

        Raises:
            IndexError: If the list is empty or the index is out of range.
        """
        if index is None:
            index = -1
        popped = super().pop(index)
        print("Popped [{}] from the list".format(popped))
        return popped
