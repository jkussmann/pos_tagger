"""
Unit tests for the POS tagger
"""

import unittest
import warnings
from sys import executable
import socket
import time
from subprocess import Popen, CREATE_NEW_CONSOLE
from pos_tagger import get_stanford_pos_tags, get_spacy_pos_tags, get_nltk_pos_tags, get_pos_tags


def ignore_warnings(test_func):
    """
    Function to ignore test warnings that are not relevant
    """
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            test_func(self, *args, **kwargs)
    return do_test

class TestPOS(unittest.TestCase):
    """
    Class for testing part of speech functions
    """
    @ignore_warnings
    def test_stanford(self):
        """
        Test for Stanford function.
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(("localhost", 9000))

        if result != 0:
            Popen(
                [executable, "core_nlp.py"],
                cwd="c:\stanford-corenlp-full-2018-02-27",
                creationflags=CREATE_NEW_CONSOLE,
            )
            print(
                "Initializing CoreNLP...."
            )  # Give CoreNLP some time to get going before accepting input.
            time.sleep(120)

        self.assertEqual(get_stanford_pos_tags("The quick brown fox jumped over the lazy dog."),
                         [('The', 'DT'), ('quick', 'JJ'), ('brown', 'JJ'), ('fox', 'NN'),
                          ('jumped', 'VBD'), ('over', 'IN'), ('the', 'DT'), ('lazy', 'JJ'),
                          ('dog', 'NN')])
        sock.close()

    @ignore_warnings
    def test_spacy(self):
        """
        Test for Spacy
        """
        self.assertEqual(get_spacy_pos_tags("The quick brown fox jumped over the lazy dog."),
                         [('The', 'DT'), ('quick', 'JJ'), ('brown', 'JJ'), ('fox', 'NN'),
                          ('jumped', 'VBD'), ('over', 'IN'), ('the', 'DT'), ('lazy', 'JJ'),
                          ('dog', 'NN'), ('.', '.')])

    @ignore_warnings
    def test_nltk(self):
        """
        Test for NLTK
        """
        self.assertEqual(get_nltk_pos_tags("The quick brown fox jumped over the lazy dog."),
                         [('The', 'DT'), ('quick', 'JJ'), ('brown', 'NN'), ('fox', 'WDT'),
                          ('jumped', 'VBD'), ('over', 'IN'), ('the', 'DT'), ('lazy', 'JJ'),
                          ('dog', 'VBG')])

    @ignore_warnings
    def test_consolidated(self):
        """
        Test for the consolidation function
        """
        self.assertEqual(get_pos_tags("The quick brown fox jumped over the lazy dog."),
                         [('The', 'DT'), ('quick', 'JJ'), ('brown', 'JJ'), ('fox', 'NN'),
                          ('jumped', 'VBD'), ('over', 'IN'), ('the', 'DT'), ('lazy', 'JJ'),
                          ('dog', 'NN')])

if __name__ == '__main__':
    unittest.main()
