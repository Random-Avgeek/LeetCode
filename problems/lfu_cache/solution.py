import collections
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.keyvalmap={}
        self.freqkeymap=collections.defaultdict(dict)
        self.minfreq=0

    def _update_freq(self,key:int)->None:
        val,freq=self.keyvalmap[key]
        del self.freqkeymap[freq][key]
        if not self.freqkeymap[freq] and self.minfreq == freq:
            self.minfreq+=1
        
        self.keyvalmap[key][1]+=1
        newfreq=freq+1
        self.freqkeymap[newfreq][key]=None
    def get(self, key: int) -> int:
        if key not in self.keyvalmap:
            return -1
        self._update_freq(key)
        return self.keyvalmap[key][0]
        

    def put(self, key: int, value: int) -> None:
        if self.capacity==0:
            return
        if key in self.keyvalmap:
            self.keyvalmap[key][0]=value
            self._update_freq(key)
            return

        if len(self.keyvalmap)>=self.capacity:
            lrukey=next(iter(self.freqkeymap[self.minfreq]))
            del self.freqkeymap[self.minfreq][lrukey]
            del self.keyvalmap[lrukey]
        
        self.keyvalmap[key]=[value,1]
        self.freqkeymap[1][key]=None
        self.minfreq=1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)