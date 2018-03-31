#######that is anther is_firend ########
def is_friend(name):
	if name[0]== "D":
		return True
	else :
	    return False
####### outputs #######		
print is_friend("Daine") #True
print is_friend("Rafeeq") #False
#######that is anther is_firend ########
def is_friend_(name):
	return name[0]=="D"
######## outputs ##########
print is_friend_("Daine")#True
print is_friend_("Rafeeq")#False	
def is_friend(name):
	if name[0]== "D" or name[0]=="N":
		return True
	else :
	    return False
print is_friend("Daine")#True
print is_friend("Rafeeq")#False
print is_friend("N")#True	    