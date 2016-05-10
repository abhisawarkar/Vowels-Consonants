def diff(string):
    L=filter(lambda x: x == "A" or x=="E" or x=="I" or x=="O" or x=="U",list(string))
    W=filter(lambda x: x not in L,list(string))
    return L, W

s=raw_input().strip()
vowels,consonents=diff(s)

	

	
