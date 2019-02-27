"""
------------------------------------------------------------------------
Midterm Practice - Question 6
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-02-13
------------------------------------------------------------------------
"""
class Set:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Set.
        Use: s = Set()
        -------------------------------------------------------
        Returns:
            Initializes an empty set.
        -------------------------------------------------------
        """
        self._values = []
        # your code here
        
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the set is empty.
        Use: b = s.is_empty()
        -------------------------------------------------------
        Returns:
            True if the set is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the set.
        Use: n = len(s)
        -------------------------------------------------------
        Returns:
            the number of values in the set.
        -------------------------------------------------------
        """
        return len(self._values)

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the set.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of key in the set, -1 if key is not found (int)
        -------------------------------------------------------
        """
        
        # your code here
        i = -1
        for n in range(len(self._values)):
            value = self._values[n]
            if value == key:
                i = n
        return i

    def insert(self, i, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the set.
        Use: b = s.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            inserted - True if the value was inserted at i, False otherwise.
                value is inserted at position i or appended to the end of the set
                if i > len(s) only if value is unique in the set (boolean)
        -------------------------------------------------------
        """
        
        # your code here
        if value in self._values:
            inserted = False
        else: # Not in
            if i > len(self._values): # Appending
                self._values.append(value)
            else: # i within index range, insert accordingly
                # Need to move everything over
                self._values.append(None) # Create an empty space at end of list
                # Traverse bw thru list up to (and incl) index i
                for n in range(len(self._values) - 1, i, -1):
                    temp = self._values[n - 1]
                    self._values[n] = temp
                self._values[i] = value
            inserted = True
        return inserted

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the set that matches key.
        Use: value = s.remove( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        
        # your code here
        
        return value

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in the set that matches key.
        Use: value = s.find( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot find in an empty set"
        
        # your code here
        
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = s.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the set (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty set"
        
        # your code here
        
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds the location of the first occurrence of key in the set.
        Use: n = s.index( key )
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the location of the full value matching key, otherwise -1 (int)
        -------------------------------------------------------
        """
        
        # your code here
        
        return i


    def _valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(set) to len(set) - 1
        Use: assert self._valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = len(self._values)
        return -n <= i < n
