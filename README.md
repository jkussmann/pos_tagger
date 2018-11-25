# Part of Speech Tagger
This is a part of speech tagger using NLTK, Spacy, and Stanford Core NLP. The results of each one is consolidated to include any tags ommitted by one of the taggers. If there is disagreement among the taggers for a word, the majority is used. If all 3 taggers disagree, Spacy is used.

## Getting Started

This code is initially written to run on a Windows 10 environment. The program is run from the command line and any IDE can be used.

### Prerequisites

What things you need to install the software and how to install them
* Python 3 (https://www.python.org/downloads/windows/)
* NLTK (https://www.nltk.org/)
* Spacy (https://spacy.io/)
* Stanford CoreNLP (https://stanfordnlp.github.io/CoreNLP/)

## Running the code

Open a command line window and change to the directory the code is located

```
c:\pos_tagger>python main.py
Initializing CoreNLP....

Enter a sentence: The quick brown fox jumped over the lazy dog.

Stanford Tagged String:
DT: The, JJ: quick, JJ: brown, NN: fox, VBD: jumped, IN: over, DT: the, JJ: lazy, NN: dog

NLTK Tagged String:
DT: The, JJ: quick, NN: brown, WDT: fox, VBD: jumped, IN: over, DT: the, JJ: lazy, VBG: dog

Spacy Tagged String:
DT: The, JJ: quick, JJ: brown, NN: fox, VBD: jumped, IN: over, DT: the, JJ: lazy, NN: dog, .: .

Consolidated POS tags:
DT: The, JJ: quick, JJ: brown, NN: fox, VBD: jumped, IN: over, DT: the, JJ: lazy, NN: dog

Enter a sentence: end
Ending Program ...

c:\pos_tagger>
```

## Author

* **John Kussmann** - *Initial work*
