

class Node:                                       #Creates a node with data that points to None

    def __init__(self,data=None):
        self.node=data
        self.next=None


class Linkedlist:

     def __init__(self):                          #Creates a head
        self.head=None


     def insert(self,data):                       #Inserting data into linkedlist

         newnode=Node(data)                       #Creates node structure with data that points to None

         temp=self.head                           #Assigning the already created list to a new object temp

         #Adding the node to end of Linked List
         if self.head==None:
            self.head=newnode
         else:
              while temp.next is not None:
                    temp=temp.next
              temp.next=newnode



     def count(self):                           #Counts the number of elements in a linkedlist

        node=self.head

        if node==None:
            return "Empty list"

        k=1

        while node.next:
              k=k+1
              node=node.next
        return(k)


     def delete(self,index):                       #Deletes an element from linkedlist given the index

        n=self.count()
        k=1
        prev=None
        node=self.head
        if n=="Empty list" or n<index:
            return("invalid index")

        while k<index:
             prev=node
             node=node.next
             k=k+1

        if prev==None:
           self.head=node.next                      #Deletes the 1st element of the list
        else:
             prev.next=node.next                    #Deletes element other than the 1st element


     def insertindex(self,data,index):              #Inserts an element from linkedlist given the index

         n=self.count()
         k=1
         prev=None
         node=self.head

         if n=="Empty list" or (n+1)<index:
            print "invalid index"
            return("invalid index")

         while k<index:
             prev=node
             node=node.next
             k=k+1
         if prev==None:
            self.insert(data)
         else:
             prev.next=Node(data)
             prev=prev.next
             prev.next=node



     def printlist(self):                #Print the list

        node=self.head
        while node!=None:
            print node.node
            node=node.next



     def invert(self):             #Reverses the list

         last=None
         current=self.head


         while current is not None:
               nxt=current.next
               current.next=last
               last=current
               current=nxt

         self.head=last
         return(last)













n=Linkedlist()
n.insert(1)
n.insert(2)
n.insert(3)
n.insert(4)
n.insert(5)
n.insertindex(10,5)
n.printlist()
n.invert()
n.printlist()

