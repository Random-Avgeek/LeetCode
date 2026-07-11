class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.size=capacity
        self.cache={} # <- for mapping key to its Node
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def insert(self,node):
        node.prev=self.head
        node.next=self.head.next
        node.next.prev=node
        self.head.next=node

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        new_node=Node(key,value)
        self.cache[key]=new_node
        self.insert(new_node)

        if len(self.cache)>self.size:
            lru=self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)