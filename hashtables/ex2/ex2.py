#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for index in range(length):
        hash_table_insert(hashtable, tickets[index].source, tickets[index].destination)
        route[0] = hash_table_retrieve(hashtable, 'NONE')

    for everyTicket in range(1, length-1):
            route[everyTicket] = hash_table_retrieve(hashtable, route[everyTicket-1])

    route.pop()
    return route
