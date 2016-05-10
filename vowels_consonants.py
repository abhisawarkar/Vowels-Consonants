#!/bin/python

def diff(string):

    V=filter(lambda x: x == "A" or x=="E" or x=="I" or x=="O" or x=="U",list(string))
    C=filter(lambda x: x not in L,list(string))

    return V, C

	

	
