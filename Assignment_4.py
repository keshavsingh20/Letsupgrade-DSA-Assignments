# # Question 1
# Implement deletion operation from the end of the linked list and Insertion operation from the
# beginning of the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def deleteNode(self):
        if self.head == None:
            return

        temp_node = self.head

        if position == 0:
            self.head = temp_node.next
            temp_node = None
            return

    def insertBeg(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
            if self.head == None:
                print("No node to display")
                return
            temp = self.head
            while temp != None:
                print(temp.data, end = " ")
                temp = temp.next

li = LinkedList()
li.insertBeg(10)
li.insertBeg(20)
li.insertBeg(30)
li.display()



# # Question 2
# Implement binary search using python language.
# (Write a function which returns the index of x in given array arr if present, else returns -1)

def binary_search(arr,low,high,x):
    if high>=low:
        mid=(high+low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr,low,mid-1,x)
        else:
            return binary_search(arr,mid+1,high,x)
    else:
        return -1

arr=[10,20,30,35,40,45]
x=int(input("Enter the element to find in the array:"))
result=binary_search(arr,0,len(arr)-1,x)


if result!=-1:
    print("Element is present at index",str(result))
else:
    print("Element is not present in array.")


# # Question 3
# Write a Python program to find the middle of a linked list.

# In[10]:


class Node: 

   def __init__(self, data): 
       self.data = data 
       self.next = None

class LinkedList: 

   def __init__(self): 
       self.head = None

   def push(self, new_data): 
       new_node = Node(new_data) 
       new_node.next = self.head 
       self.head = new_node 

   def printMiddle(self): 
       temp = self.head  
       count = 0
         
       while self.head: 
 
           # only update when count is odd 
           if (count & 1):  
               temp = temp.next
           self.head = self.head.next
 
           # increment count in each iteration  
           count += 1 
         
       print(temp.data)  


list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 





