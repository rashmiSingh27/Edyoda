def findSublists(A):
    for i in range(len(A)):


        for j in range(i, len(A)):
            print(A[i:j + 1])

def rotate(arr, n):
    x = arr[n - 1]  #last element

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = x
    print(arr)



if __name__ == '__main__':
    A = [2, 7, 5]
    B=[1, 4, 6, 8, 7]# [7, 1, 4, 6, 8]


    #findSublists(A)
    rotate(B, len(B))


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LL:
    def __init__(self):
        self.head = None

    def append1(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while (temp.next is not None):
            temp = temp.next
        temp.next = new_node
    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next is not None):
            last = last.next

        last.next = new_node

    def printLL(self):
        t= self.head

        while t:
            print(t.data, end="->>")
            t = t.next
    def rotateLL(self):
        current = self.head
        while (current):
            print(current.data, end='=>')
            current = current.next


a = LL()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.printLL()
