# Question 1: 
# Write a Python program to print even numbers in a list.
# Sample:
# Input: list1 = [12, 3, 55, 6, 144]
# Output: [12, 6, 144]
# Input: list2 = [2, 10, 9, 37]
# Output: [2, 10]

n=int(input())
list1=[]
for i in range(0,n):
    x=int(input())
    if x%2==0:
        list1.append(x)
    
print(list1)




# Question 2
# Write a program to print the following pattern
#     1
#    22
#   333
#  4444
# 55555

n=int(input())
for i in range(0,n+1):
    print(" "*(n-i),str(i)*i)






