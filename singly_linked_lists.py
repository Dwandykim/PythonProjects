class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        current = self.head     # initialize temp variable
        counter = 0             # counter to match index number
        
        while current:
            try:
                if index == counter:
                    return current.val
                counter += 1
                current = current.next
            except:
                return -1
                    
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        # Case) empty list : set head node equal to new_node
        if self.head is None:
            self.head = new_node
            return
        # Case) list not empty
        last_node = self.head
        while last_node.next:   # while loop til we get to the end of linked list
            last_node = last_node.next 
        last_node.next = new_node
    
    def getCount(self):
        # supplementary function to get length of linked list
        temp = self.head
        count = 0 
        
        while temp:
            count += 1
            temp = temp.next
            
        return count 
        
    def addAtIndex(self, index: int, val: int) -> None:
        # Add a node of value val before indexed node 
        # If len(index) = len(linked_list), then append at end
        # Finally, if len(index) > len(linked_list), then node will not be inserted
        new_node = Node(val)
        
        len_linked_lst = self.getCount()
        
        if index > len_linked_lst:
            return
        elif index == len_linked_lst:
            last_node = self.head
            while last_node.next:   # while loop til we get to the end of linked list
                last_node = last_node.next 
            last_node.next = new_node
        else:    
            temp = self.head
            count = 1
            while temp != None and count < index:
                temp = temp.next
                count += 1
            
            new_node.next = temp.next 
            temp.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        
        if index == 0:
            self.head = self.head.next
        else:    
            temp = self.head
            counter = 1
            while temp != None and counter < index:  # to get the node right before the index 
                temp = temp.next
                counter += 1
            # delete the note
            temp.next = temp.next.next
            

    def __str__(self):
        # defining a blank res variable
        res = ""
         
        # initializing ptr to head
        ptr = self.head
         
        # traversing and adding it to res
        while ptr:
            res += str(ptr.val) + ", "
            ptr = ptr.next
 
        # removing trailing commas
        res = res.strip(", ")
        
        # chen checking if
        # anything is present in res or not
        if len(res):
            return "[" + res + "]"
        else:
            return "[]"
        
linked_lst = MyLinkedList()
linked_lst.addAtHead(4)
linked_lst.addAtHead(3)
linked_lst.addAtTail(10)
linked_lst.addAtHead(1)
linked_lst.addAtIndex(4, 2)
print(linked_lst)
print(linked_lst.get(2))
linked_lst.deleteAtIndex(2)
print(linked_lst)
