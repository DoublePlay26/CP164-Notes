"""
-------------------------------------------------------
Circular array version of the Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2018-10-11"
-------------------------------------------------------
"""
from copy import deepcopy


class Queue:

    def __init__(self, max_size):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a fixed-size list.
        Use: cq = Queue(max_size)
        -------------------------------------------------------
        Parameters:
            max_size - maximum size of the queue (int > 0)
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        assert max_size > 0, "Queue size must be > 0"

        self._max_size = max_size
        self._values = [None] * self._max_size
        self._front = 0
        self._rear = 0
        self._count = 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(cq)
        -------------------------------------------------------
        Returns:
            the number of values in the queue.
        -------------------------------------------------------
        """
        # Your code here

        return

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of the queue.
        Use: cq.insert( value )
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert (self._count < self._max_size), 'queue is full'

        # Your code here

        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = cq.is_empty()
        -------------------------------------------------------
        Returns:
            True if the queue is empty, False otherwise.
        -------------------------------------------------------
        """
        # Your code here

        return

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = cq.is_full()
        -------------------------------------------------------
        Returns:
            True if the queue is full, False otherwise.
        -------------------------------------------------------
        """
        # Your code here

        return

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: v = cq.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of the queue -
                the value is not removed from the queue (?)
        -------------------------------------------------------
        """
        assert (self._count > 0), 'Cannot peek at an empty queue'

        # Your code here

        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: v = cq.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
                removed from the queue (?)
        -------------------------------------------------------
        """
        assert (self._count > 0), 'Cannot remove from an empty queue'

        # Your code here

        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in cq:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        j = self._front
        i = 0

        while i < self._count:
            yield self._values[j]
            i += 1
            j = (j + 1) % self._max_size

