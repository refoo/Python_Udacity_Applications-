def bigger (n1,n2):
	if n1>n2:
		return n1
	return n2	

def biggest (n1,n2,n3):
	return bigger(n1,bigger(n2,n3))

print biggest (6,6,4)
print biggest (6,2,3)
print biggest (6,2,7)
print biggest (6,9,3)
print "__________________________"
########## anther soltion #############
def biggest_(n1,n2,n3):
	if n1 > n2 and n1 > n3 :
		return n1
	elif n2 > n1 and n2 > n3 :
	    return n2 
	elif n3 > n1 and n3 > n2 :
	    return n3
	elif n3 == n1 or n3 == n2 :
	    return n3
	elif n1 == n2 or n3 == n1 :
	    return n1        

print biggest_ (6,6,4)
print biggest_ (6,2,3)
print biggest_ (6,2,7)
print biggest_ (6,9,3)
print "__________________________" 
########## anther soltion #############
def biggest_3(n1,n2,n3):
	return max(n1,n2,n3)

print biggest_3 (6,6,4)
print biggest_3 (6,2,3)
print biggest_3 (6,2,7)
print biggest_3 (6,9,3)	
print "__________________________"
print "the test is complte"