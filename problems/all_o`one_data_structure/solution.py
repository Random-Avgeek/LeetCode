class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.key_node_map = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_after(self, prev_node, new_node):
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next.prev = new_node
        prev_node.next = new_node
    def inc(self, key: str) -> None:
        if key not in self.key_node_map:
            next_node = self.head.next
            if next_node.count != 1:
                new_node = Node(1)
                self._insert_after(self.head, new_node)
            self.head.next.keys.add(key)
            self.key_node_map[key] = self.head.next
        else:
            curr_node = self.key_node_map[key]
            next_node = curr_node.next
            new_count = curr_node.count + 1
            
            if next_node.count != new_count:
                new_node = Node(new_count)
                self._insert_after(curr_node, new_node)
                
            curr_node.next.keys.add(key)
            self.key_node_map[key] = curr_node.next
            curr_node.keys.remove(key)
            if not curr_node.keys:
                self._remove_node(curr_node)

    def dec(self, key: str) -> None:
        curr_node = self.key_node_map[key]
        
        if curr_node.count == 1:
            del self.key_node_map[key]
        else:
            prev_node = curr_node.prev
            new_count = curr_node.count - 1
            
            if prev_node.count != new_count:
                new_node = Node(new_count)
                self._insert_after(curr_node.prev, new_node)
                
            curr_node.prev.keys.add(key)
            self.key_node_map[key] = curr_node.prev
        curr_node.keys.remove(key)
        if not curr_node.keys:
            self._remove_node(curr_node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()