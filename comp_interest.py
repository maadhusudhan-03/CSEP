P=int(input("enter the total amount:"))
T=int(input("enter the number of periods:"))
R=int(input("enter the interest rate:"))
def compound(P,T,R):
	if T==0:
		return P
	else:
		return compound(P+(P*R)/100,R,T-1)
print(compound(P,T,R))
