class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

##    def getData(self):
##        return self.data
##
##    def getNext(self):
##        return self.next
##
##    def setData(self, newdata):
##        self.data = newdata
##
##    def setNext(self, newnext):
##        self.next = newnext

def printList(head):
    n = head
    #print (n.data)
    while n.next is not None:
        print (n.data + " ->" ,end =" ")
        n = n.next
        

def main():
    head = Node("head")
    choice = 1
    length = 1
    while choice is not 0:
        print ("1 = add, 2 = delete 0 = quit")
        choice = int(input())
        if choice == 1:
            print("enter data")
            data = input()
            print ("enter offset u want to add at")
            offset = input()
            if offset > lenght:
                print ("sorry try again")
                continue
            n = head
            new_node = Node(data)
            while (offset -1 ) > 0:
                n = n.next
            n.next = new_node
            printList(head)
        elif choice == 2:
            print ("in progress")
            break
        else:
            print ("error wrong choice")
            break
    
    print("bye")        
            
            
            

    printList(head)

main()
