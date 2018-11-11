import pickle
import os
import spacy
import psutil
import sys

from nltk.tag.sequential import ClassifierBasedPOSTagger
from nltk.tag import DefaultTagger
from nltk.tree import *
from nltk.corpus import treebank
from nltk.tokenize import RegexpTokenizer
from nltk.tag.stanford import CoreNLPPOSTagger
from subprocess import Popen, CREATE_NEW_CONSOLE
from sys import executable

stPOS = CoreNLPPOSTagger(url='http://localhost:9000')
tokenizer = RegexpTokenizer(r'\w+')
spacy_nlp = spacy.load('en_core_web_sm')

model_path = "models/"

if sys.version_info[0] == 3:
    unicode = str

def get_stanford_pos_tags(line):
    """
	Get part of speech tags using the Stanford POS tagger
    """	
	
    tokenized_line = tokenizer.tokenize(line)	
    line_tagged_initial = stPOS.tag(tokenized_line)    
    line_tagged_output = []
	
    for item in line_tagged_initial:            
        line_tagged_output.append((item[0], item[1]))								   
		    
    formatted_string = ', '.join('{}: {}'.format(*el[::-1]) for el in line_tagged_output)
    print ('')
    print ('Stanford Tagged String: ')
    print (formatted_string)
    print ('')
	
    return line_tagged_output	

def train_tagger():
    print ('Training POS tagger...')    
	#https://github.com/japerk/nltk3-cookbook/blob/master/chapter4.py
	
    tagged_sentences = treebank.tagged_sents()
    size = int(len(tagged_sentences) * 0.9)
    train_sents = tagged_sentences[:size]	
    test_sents = tagged_sentences[3000:]

    default = DefaultTagger('NN')	
    tagger = ClassifierBasedPOSTagger(train=train_sents, backoff=default, cutoff_prob=0.3)
    print (tagger.evaluate(test_sents))  # 0.9613641269156055  
	
	# save model to pickle file as binary
    file_name = model_path + 'tag_model.pkl'
    with open(file_name, 'wb') as fout:
        pickle.dump(tagger, fout)
		
    print ('model written to: ' + file_name)
    print ('')
	
    return tagger
	
def get_pos_tagger():
    # check if models exist, if not run training    
    if(os.path.isfile(model_path + 'tag_model.pkl') == False):
	    print ('')
	    print ('Creating Tag Model.....')
	    tagger = train_tagger()
    else:	    
		# read the file in as binary
	    tagger = pickle.load(open(model_path + 'tag_model.pkl', 'rb'))
		
    return tagger

def get_NLTK_pos_tags(line):
    """
    Get the part of speech tags using the nltk classifier tagger
    """     
	
    tagger = get_pos_tagger()
    tokenized_line = tokenizer.tokenize(line)
    tag_list = tagger.tag(tokenized_line)  
    line_tagged_output = []
	
    for item in tag_list:            
        line_tagged_output.append((item[0], item[1]))								   
	    
    formatted_string = ', '.join('{}: {}'.format(*el[::-1]) for el in line_tagged_output)
    print ('NLTK Tagged String: ')
    print (formatted_string)
    print ('')
 
    return line_tagged_output
	
def get_Spacy_pos_tags(line):
	"""
	Get the part of speech tags using the Spacy tagger
	"""

	tagged_line = spacy_nlp(line)
	line_tagged_output = []
	for word in tagged_line:
		line_tagged_output.append((str(word), str(word.tag_)))

	formatted_string = ', '.join('{}: {}'.format(*el[::-1]) for el in line_tagged_output)
	print ('Spacy Tagged String: ')
	print (formatted_string)
	print ('')

	return line_tagged_output
    
def get_pos_tags(line):
    """
	Consolidate the tags from NLTK, Spacy, and Stanford
	"""
	
    stanford_list = get_stanford_pos_tags(line)
    nltk_list = get_NLTK_pos_tags(line)
    spacy_list = get_Spacy_pos_tags(line)

    temp_list = []
    final_list = []

    for item1 in stanford_list:
        for item2 in nltk_list:
            if item1[0] == item2[0]:
                if item1[1] != item2[1]:
                    temp_list.append((item1[0], item1[1])) #Use Stanford tags if there is disagreement
                else:
                    temp_list.append((item2[0], item2[1]))

    for item3 in temp_list:
        for item4 in spacy_list:
            if item3[0] == item4[0]:
                if item3[1] != item4[1]:
                    final_list.append((item4[0], item4[1])) #Use Spacy tags if there is disagreement
                else:
                    final_list.append((item3[0], item3[1]))

    print ('Consolidated POS tags:')
    print (final_list)

def get_input():
	line = ''
	verbose_flag = False

	#Start the Stanford CoreNLP server
	proc1 = Popen([executable, 'core_nlp.py'], cwd='c:\stanford\corenlp-full-2017-06-09', creationflags=CREATE_NEW_CONSOLE)

	try:
		while (line != 'end'):
			line = input('\r\n' + 'Enter a sentence: ')
			if line == 'end':
				print ('Ending Program ...')
				sys.exit()
			else:
				get_pos_tags(line)

	except KeyboardInterrupt:
		sys.exit()

def main():
    """
    This is the main entry point for the program
    """    
	
    get_input()
    
if __name__ == "__main__":
    main()	