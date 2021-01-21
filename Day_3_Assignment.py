# # Question 1:
# Write a Python program to add two numbers using class and object.
# (Take both numbers as input from the user)

class Add:

    def findsum(self, a, b):
        s = a + b
        return s

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

obj = Add()
s = obj.findsum(a, b)

print("Sum is:", s)



# # Question 2:
# Define a function swap that should swap two values and print the swapped variables outside the
# swap function.

def swap(a,b):
    a,b=b,a
    print("After swap a is:",a)
    print("After swap b is:",b)


a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
swap(a,b)






