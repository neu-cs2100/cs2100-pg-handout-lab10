"""
Implement union-find with Users as nodes.

Add two attributes to User:
1: parent: the User who is this User's parent in the union-find algorithm
2: rank: an int which represents the node's rank (or height in the tree) for the union-find algorithm

Add these two methods to User:
1: def find(self) -> User: finds this User's root / representative node (the "find" step in the union-find algorithm)
2: def union(self, other: User) -> None: combines the sets containing this node and other into a single set (the "union" step of the union-find algorithm)

Also, complete the __hash__ method.
"""


class User:
    # Keeps track of one person, or a node in a social media graph
    def __init__(self, name: str):
        self.name = name
        self.friends: set[User] = set()

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.name == other.name
        return False

    def __hash__(self) -> int:
        # TODO
        pass

    def add_friend(self, friend: "User") -> None:
        self.friends.add(friend)
        friend.friends.add(self)
