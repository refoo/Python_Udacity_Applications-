sentence = "A NOUN went on a walk. It can VERB really fast"
sentence_s = sentence [:sentence.find("NOUN")]+sentence [sentence.find("NOUN")+4 :sentence.find("VERB")]+sentence[sentence.find("VERB")+4:]
print sentence_s