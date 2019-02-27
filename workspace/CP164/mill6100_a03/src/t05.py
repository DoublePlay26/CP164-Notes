"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-02-13
------------------------------------------------------------------------
"""
from functions import has_balanced_brackets

BALANCED = 0
MORE_LEFT = 1
MORE_RIGHT = 2
MISMATCHED = 3

#string = "(sin(x) + 2)([3+2])"    # Balanced
#string = "((sinx + 2)([3+2])"     # More Left
#string = "{a x 2 - [(c - d) x 4]})"# More Right
string = "{a x 2 - [(c - d) x 4}]"# Mismatched

balanced = has_balanced_brackets(string)

if balanced == BALANCED:
    print("'{}' has balanced brackets".format(string))
elif balanced == MORE_LEFT:
    print("'{}' has more opening brackets than closing brackets".format(string))
elif balanced == MORE_RIGHT:
    print("'{}' has more closing brackets than opening brackets".format(string))
elif balanced == MISMATCHED:
    print("'{}' has mismatched brackets".format(string))
