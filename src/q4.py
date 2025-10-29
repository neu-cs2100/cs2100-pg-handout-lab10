import sys

sys.path.append(".")
from src.q3 import User

"""
Use your implementation of union-find to find cliques. 
A clique is a set of Users where everybody in the set is friends 
with at least one other person in the set, and none of them are 
friends with someone outside the set.

There are comments to help, but you will need to write documentation.
"""


def print_cliques(users: list[User]) -> None:
    # Step 1. Make every user the representative of their own clique. (Make them their own parent.)
    # Step 2. Iterate through all the "edges" in this friend graph. Do this by iterating through
    #    all the Users, and for each User, iterate through their set of friends -- this is the set
    #    of "edges" which are connected to this "node" in the graph.
    # Step 3. For each edge, perform the union operation for the two Users so that these two Users
    #    are in the same disjoint set ("clique").
    # Step 4. After doing that for every edge in the graph, the union-find operation is complete,
    #    and we now need to print the cliques. To do that, we first need to collect the cliques
    #    into a single data structure. One way to do that is to put them into a dictionary where
    #    the keys are the roots of the trees (the "representative node" of each clique tree) and
    #    the values are the sets of members that belong to that clique. To do that, iterate through
    #    all the Users, and for each person, perform the find operation to find the representative
    #    node for the clique to which it belongs. Then, add it to the dictionary so that the key
    #    is the representative node, and the value set contains the person. Once every User has
    #    been added to a set in the dictionary, print the dictionary's contents with this formatting:
    #    "Clique led by User1: User1, User2, ..."
    #    where User1 is the representative node for that clique, and User1, User2, ... are the members
    #    of that clique, sorted alphabetically by name.
    pass
