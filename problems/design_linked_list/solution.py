class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class MyLinkedList:

    def __init__(self):
        self.head=None
        self.size=0

    def get(self, index: int) -> int:
        if index==0:
            if self.head:
                return self.head.val
            else:
                return -1
        curr=self.head
        while curr:
            if index==0:
                return curr.val
            curr=curr.next
            index-=1
        return -1

    def addAtHead(self, val: int) -> None:
        new=ListNode(val)
        if self.head:
            new.next=self.head
            self.head=new
            self.size+=1
            return
        else:
            self.head=new
            self.size+=1
            return

    def addAtTail(self, val: int) -> None:
        new=ListNode(val)
        if not self.head:
            self.head=new
            self.size+=1
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new
        new.next=None
        self.size+=1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size:
            return
        if index==0:
            new=ListNode(val,self.head)
            self.head=new
            self.size+=1
            return
        curr=self.head
        for _ in range(index-1):
            curr=curr.next
            if curr==None:
                return
        new=ListNode(val,curr.next)
        curr.next=new
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index>=self.size:
            return
        if index==0:
            if not self.head:
                return
            self.head=self.head.next
            self.size-=1
            return
        curr=self.head
        for _ in range(index-1):
            curr=curr.next
        curr.next=curr.next.next
        self.size-=1
        return

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)