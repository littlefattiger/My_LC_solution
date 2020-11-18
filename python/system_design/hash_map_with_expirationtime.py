# implement a class that store key and value, and also identity the expiration time

from heapq import heappush, heappop
from datetime import datetime, timedelta 
class solution():
    def __init__(self):
        self.d = dict()
        # A -> (25, 12:00:05)
        self.l = [] # expire keys
    def put(self, key, val, time_limit):
        
        self.d[key] = (val, datetime.now() + timedelta(seconds = time_limit))
        heappush(self.l, (datetime.now() + timedelta(seconds = time_limit), key))
        print('put value successfully')
    
    def get(self, key):
        if key not in self.d:
            return 'Key Not Found'
        value, time_limit = self.d[key]
        if  datetime.now() <= time_limit:
            return 'The value is:' + str(value)
        else:
            return 'Key Not Found'
    def clean(self):
        while self.l[0] < datetime.now():
            key = heappop(self.l)[1]
            if self.d[key][1] < datetime.now():
            
                del self.d[key]
            else:
                continue
s.put('A', 25, 5)
s.get('A')
