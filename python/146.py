# remove from list
# remove from tail
# insert into head, used double linked list can reach o 1 time


# https://leetcode.com/problems/lru-cache/
# orderdict solution: 

class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity   

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        val = self.dict.pop(key)  #Remove it first before inserting it at the end again
        self.dict[key] = val   
        return val        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:    
            self.dict.pop(key)
        else:
            if len(self.dict) == self.capacity:
                del self.dict[next(iter(self.dict))]         
        self.dict[key] = value

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

class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity   

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        val = self.dict.pop(key)  #Remove it first before inserting it at the end again
        self.dict[key] = val   
        return val        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:    
            self.dict.pop(key)
        else:
            if len(self.dict) == self.capacity:
                del self.dict[next(iter(self.dict))]         
        self.dict[key] = value
# linked list
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = dict() # key to node
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:             # similar to get()        
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.value = value         # replace the value len(dic)
        else: 
            if len(self.dic) >= self.capacity:
                self.removeFromTail()
            node = ListNode(key,value)
            self.dic[key] = node
            self.insertIntoHead(node)
			
    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insertIntoHead(self, node):
        headNext = self.head.next 
        self.head.next = node 
        node.prev = self.head 
        node.next = headNext 
        headNext.prev = node
    
    def removeFromTail(self):
        if len(self.dic) == 0: return
        tail_node = self.tail.prev
        del self.dic[tail_node.key]
        self.removeFromList(tail_node)
