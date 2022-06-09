refstr=input("enter a refference string:");
inputstr=input("enter a input string:");
refdict={}
for i in refstr:
	refdict[i]=refdict.get(i,0)+1;
inputdict={}
for i in inputstr:
	inputdict[i]=inputdict.get(i,0)+1;
if refdict==inputdict:
	print(inputstr+" is anagram of the "+refstr);
else:
	print(inputstr+" is not anagram of the "+refstr);

