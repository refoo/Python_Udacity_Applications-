
def madlibe(NOUN,VERB):
	sentence = "A NOUN went on a walk. it can VERB really fast"
	a = sentence[:sentence.find("NOUN")]
	b = sentence[sentence.find("NOUN")+4:sentence.find("VERB")]
	c = sentence[sentence.find("VERB")+4:]
	sentence_s =  a + NOUN + b + VERB + c
	return sentence_s 
print madlibe ("dog","run")	