#!/usr/bin/env python3
"""
Shapes, Interfaces, and Duck Typing
"""


class CountedIterator:
    """
    An iterator that counts the number of items iterated over.

    Attributes:
    - data (list): The data to be iterated over.
    - index (int): The current index of the iterator.
    - count (int): The number of items iterated over.
    """

    def __init__(self, data):
        """
        Initializes a new CountedIterator object.

        Args:
            data (list): The data to be iterated over.
        """
        self.data = data
        self.index = 0
        self.count = 0

    def __iter__(self):
        """
        Returns the iterator object.

        Returns:
            The iterator object.
        """
        return self

    def __next__(self):
        """
        Returns the next item in the iteration.

        Returns:
            The next item in the iteration.

        Raises:
            StopIteration: If the end of the iteration is reached.
        """
        if self.index >= len(self.data):
            raise StopIteration
        item = self.data[self.index]
        self.index += 1
        self.count += 1
        return item

    def get_count(self):
        """
        Returns the number of items iterated over.

        Returns:
            The number of items iterated over.
        """
        return self.count
