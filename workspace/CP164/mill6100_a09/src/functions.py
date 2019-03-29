"""
------------------------------------------------------------------------
Assignment 9 functions module
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-25
------------------------------------------------------------------------
"""
from Word import Word

def insert_words(fv, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in fv and inserts into
    a Hash_Set.
    -------------------------------------------------------
    Parameters:
        fv - the already open file containing data to evaluate (file)
        hash_set - the Hash_Set to insert the words into (Hash_Set)
    Returns:
        Each Word object in hash_set contains the number of comparisons
        required to insert that Word object from file_variable into hash_set.
    -------------------------------------------------------
    """
    fv.seek(0)
    lines = fv.readlines()
    
    for line in lines:
        #print("[{}]".format(line.rstrip()))
        words = line.split(' ')
        for word in words:
            if word.isalpha():
                #print("Word: {}".format(word))
                # Ignoring any punctuation and words with punctuation
                _word = Word(word.lower())
                hash_set.insert(_word)
    return

def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    -------------------------------------------------------
    Parameters:
        hash_set - a hash set of Word objects (Hash_Set)
    Returns:
        total - the total of all comparison fields in the Hash_Set
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """
    total_comparisons = 0
    max_word = Word('aaa')
    for word in hash_set:
        if word.comparisons > max_word.comparisons:
            max_word = word
        total_comparisons += word.comparisons
    return total_comparisons, max_word