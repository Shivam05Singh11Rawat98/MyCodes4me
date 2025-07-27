class Node:
    def __init__(self,key,value):
        self.key = key
        self.val = value
        self.freq = 1
        self.prev = self.next = None

class LinkedList:
    def __init__(self):
        self._sentinel = Node(None, None)
        self._size = 0
        self._sentinel.next = self._sentinel.prev = self._sentinel
    
    def length(self):
        return self._size
    
    def append(self, node):
        node.next = self._sentinel.next
        node.prev = self._sentinel
        node.next.prev = node
        self._sentinel.next = node
        self._size += 1
        
    
    def pop(self, node=None):
        if self._size==0:
            return
        
        if not node:
            node = self._sentinel.prev
        
        node.next.prev = node.prev
        node.prev.next = node.next
        self._size -= 1

        return node


class LFUCache:
    def __init__(self, capacity: int):
        self._cap = capacity
        self._lru = 1
        self._freq_map = defaultdict(LinkedList)
        self._value_map = {}
        self._size=0
    
    def _update(self,node):
        freq = node.freq
        self._freq_map[freq].pop(node)

        if self._freq_map[freq].length()==0 and self._lru == freq:
            self._lru+=1
        
        node.freq+=1
        self._freq_map[freq+1].append(node)
        

    def get(self, key: int) -> int:
        if key not in self._value_map:
            return -1
        
        node = self._value_map[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self._value_map:
            node = self._value_map[key]
            self._update(node)
            node.val = value
        else:
            if self._size == self._cap:
                freq = self._lru
                node = self._freq_map[freq].pop()
                del self._value_map[node.key]
                self._size-=1
            
            node = Node(key,value)
            self._freq_map[1].append(node)
            self._lru=1
            self._value_map[key] = node
            self._size+=1

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)