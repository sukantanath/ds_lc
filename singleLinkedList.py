class Node:
    def __init__(self,data):
        self.val = data
        self.next = None
    
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.count = 0
        

    # def printList(self) -> None:
    #     temp =self.head
    #     while (temp):
    #         print(temp.data)
    #         temp = temp.next
            
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        
        node_val = -1
        curr = self.head
        cnt = 0
        if index >= self.count or index < 0:
            return -1
        
        while (cnt < index):
            curr = curr.next
            cnt += 1
            
        node_val = curr.val
        print("Got :",node_val," at position:",index)
        return node_val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.count +=1
        
        print("After add at Head:")
        #printList(self)
        temp =self.head
        while (temp):
            #print(temp.val)
            temp = temp.next
        print("Count:",self.count)    

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        
        if self.count == 0:
            self.head = new_node
        else:    
            curr_node = self.head
            while curr_node.next != None:
                curr_node = curr_node.next

            curr_node.next = new_node
        self.count +=1
        
        print("After add at tail:")
        #printList(self)
        temp =self.head
        while (temp):
            #print(temp.val)
            temp = temp.next
        print("Count:",self.count)  

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.count:
            return
        
        if index == 0:
            print("redirect to add at head,value:",val)
            self.addAtHead(val)
            return            
        elif index == self.count:
            print("redirect to add at tail,value:",val)
            self.addAtTail(val)
            return
        
        cnt  = 0
        new_node = Node(val)
        curr_node = self.head
        prev_node = curr_node
        #print("Init curr_node:",curr_node.val)
        while (cnt != index):
            #if curr_node.next != None:
            prev_node = curr_node
            curr_node=curr_node.next
            cnt +=1
        #print("Obtained:",curr_node.val,curr_node.next)       
        new_node.next = curr_node
        prev_node.next = new_node
        self.count +=1
        
        #printList(self)
        print("After add at index:")
        temp =self.head
        while (temp):
            #print(temp.val)
            temp = temp.next
        print("Count:",self.count)  
        
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.count:
            print("Index doesnt exist:")
            return
        
        if index == 0 and self.count >= 1:
            print("In here")
            self.head = self.head.next
        else:
            print("In there:")
            cnt = 0
            curr_node = self.head
            prev_node = curr_node
            while (cnt != index):
                if curr_node.next != None:
                    prev_node = curr_node
                    curr_node=curr_node.next
                    cnt += 1

            prev_node.next = curr_node.next
        
        self.count -=1
        
        print("After delete at index:")
        #printList(self)
        temp =self.head
        while (temp):
            #print(temp.val)
            temp = temp.next
        print("Count:",self.count)  
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
