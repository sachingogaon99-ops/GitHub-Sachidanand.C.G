#Logical Problems 
 #Palindrome checker

string=input("Enter a string:")
reversed_string=string[::-1]
if string==reversed_string:
    print(string,"is a palindrome")
else:
    print(string,"is not a palindrome")

    
#Reversing a string
string=input("enter a string:")
reversed_string=string[::-1]
print("reversed string is:",reversed_string)

#Armstrong number checker
no=int(input("Enter a number:"))
sum=0
n=no
while n>0:
    digit=n%10
    sum=sum+digit**3
    n=n//10
if sum==no:
    print(no,"is a armstrong")
else:
    print(no,"is not a armstrong")

    
#Length of a string without built-in function
string=input("enter a string:")
count=0
for i in string:
    count=count+1
print("length of string is:",count)


#Inverted right triangle pattern
rows=int(input("enter the no of rows:"))
for i in range(rows,0,-1):
    for j in (1,i+1):
        print("*",end=" ")
    print()
