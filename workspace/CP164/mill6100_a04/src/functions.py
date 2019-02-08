"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-02-05
------------------------------------------------------------------------
"""

from Graph import Graph, Edge
from Priority_Queue_array import Priority_Queue

def queue_is_identical(source1, source2):
    """
    ----------------
    Determines whether two given queues are identical. Entries of 
    source1 and source2 are compared and if all contents are identical
    and in the same order, returns True, otherwise returns False.
    Use: identical = queue_is_identical(source1, source2)
    ---------------
    Parameters:
        source1 - a queue (Queue)
        source2 - a queue (Queue)
    Returns:
        identical - True if source1 and source2 are identical, False otherwise. 
            source1 and source2 are unchanged. (boolean)
    ---------------
    """
    list1 = []
    list2 = []
    for i in source1:
        list1.append(i)
    for j in source2:
        list2.append(j)
    identical = list1 == list2
    return identical

def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends. The order of the values from source is preserved.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = []    # Everything with higher priority than key
    target2 = []    # Everything with lower priority than key, including key itself
    for i in range(len(source)):
        elem = source.remove()
        if elem < key:  # element is higher priority
            target1.append(elem)
        else:   # element >= key
            target2.append(elem)
    return target1, target2

def prims(graph, start_node):
    """
    -------------------------------------------------------
    Applies Prim's Algorithm to a graph.
    Use: edges, total = prims(graph, node)
    -------------------------------------------------------
    Parameters:
        graph - graph to evaluate (Graph)
        start_node - name of node to start evaluation from (str)
    Returns:
        edges - the list of the edges traversed (list of Edge)
        total - total distance of all edges traversed (int)
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    
    node_names = graph.node_names()
    distance = 0
    visited_nodes = []
    edges = []
    for node_name in node_names:
        node_edges = graph.edges_by_node(node_name)
        for edge in node_edges:
            pq.insert(edge)
            
    
    return pq
