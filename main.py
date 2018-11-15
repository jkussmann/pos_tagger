import sys
import pos_tagger as pt

from subprocess import Popen, CREATE_NEW_CONSOLE
from sys import executable

def get_input():
	line = ''

	#Start the Stanford CoreNLP server
	proc1 = Popen([executable, 'core_nlp.py'], cwd='c:\stanford-corenlp-full-2018-02-27', creationflags=CREATE_NEW_CONSOLE)

	try:
		while (line != 'end'):
			line = input('\r\n' + 'Enter a sentence: ')
			if line == 'end':
				print ('Ending Program ...')
				sys.exit()
			else:
				print ('')
				print ('Stanford Tagged String: ')
				formatted_string = ', '.join('{}: {}'.format(*el[::-1]) for el in pt.get_stanford_pos_tags(line))
				print (formatted_string)
				print ('')
				print ('NLTK Tagged String: ')
				formatted_string = ', '.join('{}: {}'.format(*el[::-1]) for el in pt.get_NLTK_pos_tags(line))
				print (formatted_string)
				print ('')
				print ('Spacy Tagged String: ')
				formatted_string = ', '.join('{}: {}'.format(*el[::-1]) for el in pt.get_Spacy_pos_tags(line))
				print (formatted_string)
				print ('')
				print ('Consolidated POS tags:')
				formatted_string = ', '.join('{}: {}'.format(*el[::-1]) for el in pt.get_pos_tags(line))
				print (formatted_string)

	except KeyboardInterrupt:
		sys.exit()

def main():
	"""
	This is the main entry point for the program
	"""    

	get_input()

if __name__ == "__main__":
	main()