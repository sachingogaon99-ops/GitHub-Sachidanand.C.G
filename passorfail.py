
m1=int(input("enter your  science marks:"))
m2=int(input("enter your  maths marks:"))
m3=int(input("enter your  kannadamarks:"))
m4=int(input("enter your  english marks:"))
m5=int(input("enter your  computerscience marks:"))
total=m1+m2+m3+m4+m5
average=total/5
if average>=85:
    print("student passed with distinction")
elif average>=60:
    print("student passed with grade B")
elif average>=45:
    print("student passed with grade C")
elif average>=35:
    print("student passed with grade D")
else:
    print("student failed")
       
          
    