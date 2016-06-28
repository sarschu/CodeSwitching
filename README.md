# CodeSwitching

This repository contains a language ID and PoS system for Latin-Middle English + Training Pipeline for other languages
It comes with trained models for Latin-Middle English but also enables you to retrain for other languages for which tree tagger models are available.
The paper related to this system has been presented at  The 10th Workshop on Language Technology for Cultural Heritage, Social Sciences, and Humanities held in conjunction with ACL 2016 in Berlin.

# System requirements
The system requirements are:
* python 2.7
* nltk.tokenize (by doing nltk.download() in any python interpreter and choosing models/punkt for download)
* CRF++ (tested with version 0.58, but I am not aware of any changes that would not allow for a lower version: https://taku910.github.io/crfpp/) 
* perl

## To run the system:


  To simply run the system you need a raw text file you want to process
  
  ```
python run.py -h
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
  -r, --retrain         train a new model
  -l lid, --model_lid=lid
                        model file for lid
  -p MODEL_POS, --model_pos=MODEL_POS
                        model file for pos


  ```
  
  If your CRF++ is not installed in the default path of CRF++ (which is /usr/local/bin), you have to specify it via the -c option.
  With -t and -d you can give the tree tagger models you want to use. It needs to point to the tree-tagger files in the cmd-folder of TreeTagger. All files must follow the fomat as included in this release, which varies slightly from the original files.
  
  Most basic run (in case you have crf installed in the default directory):
  
  ```bash
  python run.py -f test_files/test\_tag
  ```
  
  This will use the pretrained models for Latin/Middle English and run it on the file test\_tag.
  The result of the run will be test\_tag.pos\_tagged in the directory test_files. It is in conll-Format and an be read in by ICARUS which enables easy search (as described in paper forthcoming). You can ignore the other files or use them for debugging.
  
## Retrain the system
  
  If you want to tag text that is not Middle English-Latin (by why would you want that, right?), you will have to retrain with a file that follows the formating in the test\_file folder (file: test_train). The file looks like this 
  
  > token language\_id pos_tag
  
  > token2 language\_id pos_tag
  
  The file should not contain any empty lines.
  
  In addition you will need word lists for your languages that follow the format the word lists in the wordlist directory have (json dictionaries). In case you don't want to use them, this is possible but requires some effort in terms of changing the code. If you should not be able to do this, contact me.
  
  Then specify the option -r and your tagger files (and your crf directory if necessary). The tagger files are the files you can find in the cmd-dir of the tree-tagger. This tool comes with some of the tree-tagger models (but not all of the available ones). You can easily add them by downloading them from http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/. Don't forget to adjust the tagger files according to the format of the tagger files delivered with this tool.
  You change the tagger files with the -d and -t parameter (as shown in the example call below).

  You should also give names and directories for the result models by specifying -l and -p. If you don't specify those parameters, the system will write the models to the models directory and add a time stamp.

  The System will produce a bunch of output files in the directory of your input file. The important files are:
  
  * pos_model+timestamp
  * lid_model+timestamp
  
The other files can be deleted, but can also serve as debugging files in case of issues.
  
  ```bash
  python run.py -f test_files/test_train -t tree_tagger/cmd/tree-tagger-middleenglish -d tree_tagger/cmd/tree-tagger-latin -r
  ```
You can use the newly trained model files for tagging now by including them in the tagging process with the parameters -l (language model) and -p (PoS model).

