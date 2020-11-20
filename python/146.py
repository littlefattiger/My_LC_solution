


# https://leetcode.com/problems/lru-cache/
# orderdict solution: 

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.dict = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        self.dict.move_to_end(key)
        return self.dict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
            
        self.dict[key] = value
        if len(self.dict) > self.cap:
            self.dict.popitem(last=False) 

# OrderedDict.popitem(last=True)
# The popitem() method for ordered dictionaries returns and removes a (key, value) pair. The pairs are returned in LIFO order if last is true or FIFO order if false.
