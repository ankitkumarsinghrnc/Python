T=input()
T=int(T)
while T>0:
	str = input()
	j=0
	i=0
	max=0
	while j<len(str):
		if str[j]=='<':
			count1=1
			while str[i]!='>'and i in range(0,len(str)):
				if str[i]=='<':
					count1=count1+1
					
				
					
			if count1>max:
				max=count1;
			j=i
		elif str[j]=='>':
			count2=1
			while str[i]!='<'and i in range(0,len(str)):
				if str[i]=='>':
					count2=count2+1
					i=i+1
				else :
					i=i+1
			if count2>max:
				max=count2
			j=i
				
		else:
			j=j+1
	
	print(max)
	
	T=T-1
