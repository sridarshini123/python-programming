count=0
num=int(raw_input())
for i in range(2,num):
     if(num%i==0):
          count=count+1
if(count==1):
  print("it is prime")
else:
  print("not prime")
