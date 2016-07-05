#!/usr/bin/python
# -*- coding: utf-8 -*-

#usage python train_crossvalid.py folder_with_sets
from optparse import OptionParser


import sys
import os
import subprocess
from PosTag import Tagger

#make files executable
os.system('chmod  -R +x ../')
parser = OptionParser()

parser.add_option("-f", "--file", dest="filename",
                  help="read input from FILE", metavar="FILE")
parser.add_option("-c", "--crf_dir", dest="crf",
                  help="installation directory of CRF", metavar="CRF_DIR")
parser.add_option("-t", "--treetagger_l1", dest="treetagger_l1",
                  help="installation directory of TreeTagger call-script one", metavar="TT_l1") 
parser.add_option("-d", "--treetagger_l2", dest="treetagger_l2",
                  help="installation directory of TreeTagger call-script one", metavar="TT_l2") 
parser.add_option("-r", "--retrain",
                  action="store_true", dest="training", default=False,
                  help="train a new model")
parser.add_option("-z", "--testing",
                  action="store_true", dest="testing", default=False,
                  help="test with gold standard data")                 
parser.add_option("-l", "--model_lid", dest="model_lid",
                  help="model file for lid", metavar="lid") 
parser.add_option("-p", "--model_pos", dest="model_pos", help="word list with POS for language 1")
parser.add_option("-w", "--wordlist1", dest="wordlist1",
                  help="model file for lid", metavar="lid") 
parser.add_option("-v", "--wordlist2", dest="wordlist2", help="word list with POS for language 2")
parser.add_option("-k", "--no_tokenize",
                  action="store_false", dest="tokenize", default=True,
                  help="use pretokenized text, one tok per line")
                  

(options, args) = parser.parse_args()
print options


defined_options=[]
if not options.filename:
    parser.error('Option --file (-f) must be specified.')
if not options.crf:
    
    out = subprocess.check_output("which crf_learn",shell=True)
    #out, err = proc.communicate()

    if out.strip() !='/usr/local/bin/crf_learn':
        parser.error('Option --crf_dir (-c) must be specified because your CRF++ is not installed in /usr/local/bin')


options= vars(options)
filtered_opt={k: v for k, v in options.items() if v}
tagger = Tagger(**filtered_opt)
tagger.run()


