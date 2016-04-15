# CodeSwitching
This repository contains a language ID and PoS system for Latin-Middle English + Training Pipeline for other languages


# System requirements
The system requirements are:
* python 2.7
* nltk.tokenize
* CRF++ (tested with version 0.58, but I am not aware of any changes that would not allow for a lower version) 
* perl

# To run the system:
  To simply run the system you need a raw text file you want to process
  
  code([ python run.py -h
Usage: run.py [options]

Options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  read input from FILE
  -c CRF_DIR, --crf_dir=CRF_DIR
                        installation directory of CRF
  -t TT_l1, --treetagger_l1=TT_l1
                        installation directory of TreeTagger call-script one
  -d TT_l2, --treetagger_l2=TT_l2
                        installation directory of TreeTagger call-script one
  -r, --retrain         train a new model)
  
  If your CRF++ is not installed in the default path, you have to specify it via the -c option
  
  with -t and -d you can give the tree tagger models you want to use. It needs to point to the tree-tagger files in the cmd-folder of TreeTagger. All files must follow the fomat as included in this release, which varies slightly from the original files.
  
  # To retrain the system
  
  If you want to tag text that is not Middle English-Latin (by why would you want that, right?), you will have to retrain with a file that follows the formating in the test_file folder (file: test_train) 
  Then specify the option -r and your tagger files (and your crf directory if necessary)
  The System will produce a bunch of output files in the directory of your input file. The important files are:
  * 
