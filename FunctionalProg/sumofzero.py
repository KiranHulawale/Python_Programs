x=[-1,-2,-4,-5,1,2,3,4,5]
for i in range(0,len(x)):
	for j in range(i+1,len(x)):
		for k in range(j+1,len(x)):
			if x[i]+x[j]+x[k]==0:
				print(x[i],x[j],x[k])