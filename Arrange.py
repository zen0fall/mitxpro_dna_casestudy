def arrange(set1,c):
	len1 = len(set1)
	
	if len1!=2:
		
		for i in range(0,len1):
			X=c+str( set1[i])
			set2=[]
			for j in range(0,len1):
				if i!=j:
					set2.append(set1[j])
			arrange(set2,X)
	else:
		print c+str(set1[0])+str(set1[1])
		print c+str(set1[1])+str(set1[0])
		c=""

def arrange2(set1,c,result): #usage: arrange2(set1,c='',result=[])
    len1 = len(set1)
    
    if len1!=2:

        for i in range(0,len1):
            X=c+str( set1[i])
            set2=[]
            for j in range(0,len1):
                if i!=j:
                    set2.append(set1[j])
            arrange(set2,X,result)
    else:
        
        #print(c+str(set1[0])+str(set1[1]))
        r1 =c+str(set1[0])+str(set1[1])
        result.append(r1)
        #print (c+str(set1[1])+str(set1[0]))
        r2 =c+str(set1[1])+str(set1[0])
        result.append(r2)
        
        c=""
        #return result				
