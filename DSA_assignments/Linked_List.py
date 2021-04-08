class Node:
 
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next



class LinkedList:
    def __init__(self):
        self.head = None

  
    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next is not None):
            last = last.next

        last.next = new_node

   
    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(new_data)

        new_node.next = prev_node.next

        prev_node.next = new_node

    def length(self):
        temp = self.head
        count = 0
        while (temp is not None):
            temp = temp.next
            count += 1

        return count

    
    def printLL(self):
        current = self.head
        while (current):
            print(current.data, end='=>')
            current = current.next
            
    def rotate(self, k):

        if k == 0:
            return
        curr = self.head
        c = 1
        while (c < k and curr):
            curr = curr.next
            c+=1# 50
        if curr is None:
            return
        knode = curr
        while (curr.next is not None):
            curr = curr.next  # 60
        curr.next = self.head
        self.head = knode.next
        knode.next = None
        
    def detectLoop(self):
        s=set()
        temp=self.head
        while(temp):
            if temp in s:
                #print("loop found")
                return True
            s.add(temp)
            temp=temp.next
        return False
    
    def removeLL(self,k):
        temp = self.head

        if (temp is not None):
            if (temp.data == k):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == k:
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return


        prev.next = temp.next

        temp = None
      



if __name__ == '__main__':
    llist = LinkedList()

    llist.append(5)
    llist.append(7)
    llist.append(8)
    llist.append(9)

    # llist.insertAfter(llist.head, 6)
    #llist.printLL()
    #llist.removeLL(8)
    llist.printLL()
    llist.rotate(5)#5 for last elemnt on first 

    print("\nRotated Linked list")
    llist.printList()
    # length = llist.length()
    # print("\nlength of linked list is {}".format(length))
    llist.head.next.next.next.next = llist.head    
    if (llist.detectLoop ()):
        print ("\nLoop found")
    else:
        print ("\nNo Loop ")
