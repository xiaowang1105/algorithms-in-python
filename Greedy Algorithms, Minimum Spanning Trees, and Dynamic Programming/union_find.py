class Union_Find:
    """class for union find data structure

    >>> a, b, c = Union_Find(), Union_Find(), Union_Find()
    >>> [a.rank, b.rank, c.rank]
    [0, 0, 0]
    >>> c == Union_Find.union(c, a)
    True
    >>> b == Union_Find.union(a, b)
    True
    >>> [a.rank, b.rank, c.rank]
    [1, 0, 0]
    """
    def __init__(self):
        self.parent = self
        self.rank = 0
    def find_set(self):
        if self.parent != self:
            self.parent = self.parent.find_set()
        return self.parent
    @staticmethod
    def link(x, y):
        if x.rank > y.rank:
            delete = y.parent
            y.parent = x
        else:
            delete = x.parent
            x.parent = y
            y.rank = y.rank + 1 if x.rank == y.rank else y.rank
        return delete
    @classmethod
    def union(cls, x, y):
        return cls.link(x.find_set(), y.find_set())

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
