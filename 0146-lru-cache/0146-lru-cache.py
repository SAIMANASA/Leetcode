class Node:
    def __init__(self,key,val):
        self.key = key 
        self.val = val
        self.prev = self.next = None
class LRUCache:
    """
    # using list will exceed the time so, we need to comeup with doublelinked list 
    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity
        

    def get(self, key: int) -> int:

        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                temp = self.cache.pop(i)
                self.cache.append(temp)
                return temp[1]
        return -1

        

    def put(self, key: int, value: int) -> None:

        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                temp = self.cache.pop(i)
                temp[1] = value
                self.cache.append(temp)
                return 

        if self.capacity == len(self.cache):
            self.cache.pop(0)
        
        self.cache.append([key,value])

    """        

    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #maps to the double linked list 
        self.left , self.right = Node(0,0) , Node(0,0)
        self.left.next ,self.right.prev = self.right , self.left
    
    def insert(self,node):
        prev,nxt = self.right.prev , self.right
        prev.next = nxt.prev = node
        node.next ,node.prev = nxt , prev

        
        
    
    def remove(self,node):
        prev , nxt = node.prev , node.next 
        prev.next = nxt
        nxt.prev  = prev 
        
    def get(self, key: int) -> int:
        
        if key in self.cache:
            self.remove(self.cache[key])

            self.insert(self.cache[key])

            return self.cache[key].val
        return - 1

        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
    
        if self.capacity < len(self.cache):
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
    

    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)