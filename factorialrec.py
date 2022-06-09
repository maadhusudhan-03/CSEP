num=int(input("enter the input number:"))
def factorial(n):
	if n==1:
		return n
	else:
		return n*factorial(n-1)
if num<0:
	print("Please enter a valid input");
elif num==0:
	print("the factorial of 0 is 1");
else:
	
	print("the factorial of ",num," is:",factorial(num))
	
	
