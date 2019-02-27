"""
------------------------------------------------------------------------
Assignment 3 - Function Definitions
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-27
------------------------------------------------------------------------
"""
from Stack_array import Stack

def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    contents = []
    for element in source:
        contents.append(source.pop())
        
    for element in contents:
        source.push(element)
        
def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack. 
    When finished, the contents of source1 and source2 are interlaced 
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    # Determine which stack is the shortest, going to loop over that
    #shortest_stack = source2 if len(source1) > len(source2) else source1
    shortest_stack = None
    other_stack = None
    if len(source1) > len(source2):
        shortest_stack = source2
        other_stack = source1
    else:
        shortest_stack = source1
        other_stack = source2
        
    target = Stack()
    
    # Loop and append until shortest stack is empty
    while not shortest_stack.is_empty():
        val1 = shortest_stack.pop()
        val2 = other_stack.pop()
        target.push(val1)
        target.push(val2)
        
    # Handle the rest of the elements in the longer stack
    for element in other_stack:
        target.push(element)
    return

# Constants
BALANCED = 0
MORE_LEFT = 1
MORE_RIGHT = 2
MISMATCHED = 3

def has_balanced_brackets(string):
    """
    -------------------------------------------------------
    Determines if a string contains balanced brackets or not. Non-bracket
    characters are ignored. Uses a stack. Brackets include {}, [], (), <>.
    Use: balanced = has_balanced_brackets(string)
    -------------------------------------------------------
    Parameters:
        string - the string to test (str)
    Returns:
        balanced (int) -
            BALANCED if the brackets in string are balanced
            MISMATCHED if the brackets in string are mismatched
            MORE_RIGHT if there are more right brackets than left in string
            MORE_LEFT if there are more left brackets than right in string
    -------------------------------------------------------
    """
    s = Stack()
    balanced = BALANCED
    
    OPEN_BRACKETS = "([{<"
    CLOSING_BRACKETS = ")]}>"
    
    char_index = 0
    while balanced == BALANCED and char_index < len(string):
        # Get current character we are processing
        char = string[char_index]
        if char in OPEN_BRACKETS:   # Push any opening bracket we see onto the stack
            s.push(char)
        elif char in CLOSING_BRACKETS:  # Check if top of stack matches closing brackets
            if s.is_empty():    # If stack is empty but we see a closing bracket
                balanced = MORE_RIGHT
            else:
                top = s.pop()
                # Get index of bracket at top of stack in OPEN_BRACKETS
                index = 0
                for i in range(len(OPEN_BRACKETS)):
                    if top == OPEN_BRACKETS[i]:
                        index = i
                # Index of closing bracket should be same as open bracket
                complimentary_bracket = CLOSING_BRACKETS[index]
                if not char == complimentary_bracket:
                    balanced = MISMATCHED
        char_index += 1
    if not s.is_empty():  # If we still have opening brackets in the stack but we reach the end of the string
        balanced = MORE_LEFT
        
    return balanced

# Constants
OPERATORS = "+-*/"

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    s = Stack()
    
    expression = string.split(" ")  # Split on spaces
    
    for char in expression:
        if char in OPERATORS:
            # Order that we pop is important
            operand2 = s.pop()
            operand1 = s.pop()
            
            if char == OPERATORS[0]:    # Addition
                value = operand1 + operand2
            elif char == OPERATORS[1]:   # Subtraction
                value = operand1 - operand2
            elif char == OPERATORS[-2]: # Multiplication
                value = operand1 * operand2
            elif char == OPERATORS[-1]: # Division, do not have to worry about division by zero
                value = operand1 / operand2
            s.push(value)
        else:   # Dealing with a numeric value
            s.push(int(char))
    
    answer = s.pop()    # Answer should be the only thing left in the stack
    return answer

def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    s = Stack()
    palindrome = True
    
    CHARACTERS = "abcdefghijklmnopqrstuvwxyz"
    
    if not len(string) % 2 == 0:
        mid = len(string) // 2 + 1
    else:
        mid = len(string) // 2
    
    char_index = 0
    while palindrome:
        char = string[char_index]
        
        if char in CHARACTERS:
            if char_index < mid:   # First half of string
                pass
        
        char_index += 1
    
    return palindrome