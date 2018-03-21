n=int(raw_input())
sum=0
temp=n
while(n>0):
	rem=n%10
	sum=sum*10+rem
	n=n/10
if(sum==temp):
 print("palindrome")
else:
 print("not a palindrome")
