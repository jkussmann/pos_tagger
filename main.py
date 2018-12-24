"""
This module is used to call the functions of the pos tagger
"""

import sys
from sys import executable
import socket
import time
from subprocess import Popen, CREATE_NEW_CONSOLE
import pos_tagger as pt

def get_input():
    """
	This function gets the input from the user
	"""
    line = ""

    # Start the Stanford CoreNLP server if it isn't running
    result = core_nlp_status()
    if result != 0:
        Popen(
            [executable, "core_nlp.py"],
            cwd="c:\stanford-corenlp-full-2018-02-27",
            creationflags=CREATE_NEW_CONSOLE,
        )
        print(
            "Initializing CoreNLP...."
        )  # Give CoreNLP some time to get going before accepting input.
        time.sleep(30)

    try:
        while line != "end":
            line = input("\r\n" + "Enter a sentence: ")
            if line == "end":
                print("Ending Program ...")
                sys.exit()
            else:
                print("")
                print("Stanford Tagged String: ")
                formatted_string = ", ".join(
                    "{}: {}".format(*el[::-1]) for el in pt.get_stanford_pos_tags(line)
                )
                print(formatted_string)
                print("")
                print("NLTK Tagged String: ")
                formatted_string = ", ".join(
                    "{}: {}".format(*el[::-1]) for el in pt.get_nltk_pos_tags(line)
                )
                print(formatted_string)
                print("")
                print("Spacy Tagged String: ")
                formatted_string = ", ".join(
                    "{}: {}".format(*el[::-1]) for el in pt.get_spacy_pos_tags(line)
                )
                print(formatted_string)
                print("")
                print("Consolidated POS tags:")
                formatted_string = ", ".join(
                    "{}: {}".format(*el[::-1]) for el in pt.get_pos_tags(line)
                )
                print(formatted_string)

    except KeyboardInterrupt:
        sys.exit()

def core_nlp_status():
    """
	This function gets the status of Stanford core NLP
	"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(("localhost", 9000))

    return result

def main():
    """
	This is the main entry point for the program
	"""

    get_input()

if __name__ == "__main__":
    main()
