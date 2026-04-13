#Aim: Factorial of a given no
#Coder:SHAIKH MOHD AYYAN TOUFIQ
#Class: F.E COMPS  DIV: C  ROLL NO:1
#DATE:30-JAN-26

a = int(input("Enter Number: "))
if a<0:
    print(f"Factorial of {a} is Not Defined")
fact = 1
for x in range(1,a+1):
    fact = fact*x
print(f"Factorial of {a} is",fact)
