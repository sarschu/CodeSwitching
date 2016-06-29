#!/usr/bin/env python

# -*- coding: utf-8 -*-

import sys
import codecs
import os
import subprocess
import re
import sys
import json

ud_lines= codecs.open(sys.argv[1],'r','utf8').readlines()


        


worddict={'ADJ':[],'ADP':[],'ADV':[],'AUX':[],'CONJ':[],'DET':[],'INTJ':[],'PROPN':[],"NOUN":[],'PRON':[],'VERB':[]}

for line in ud_lines:
    ls=line.split('\t')
    if len(ls)==10:
        word,tag=ls[1],ls[3]
        if tag.strip().startswith('ADJ'):
            worddict["ADJ"].append(word.strip())
        elif tag.strip().startswith("ADV"):
            worddict["ADV"].append(word.strip())
        elif  tag.strip().startswith("V"):
            worddict["VERB"].append(word.strip())
        elif tag.strip().startswith("AUX"):
            worddict["AUX"].append(word.strip())
        elif tag.startswith("ADP"):
            worddict["ADP"].append(word.strip())
        elif tag.strip()== "CONJ":
            worddict["CONJ"].append(word.strip())
        elif tag.strip()== "DET":
            worddict["DET"].append(word.strip())
        elif tag.strip()=='INTJ':
            worddict["INTJ"].append(word.strip())
        elif tag.strip()== "NOUN":
            worddict["NOUN"].append(word.strip())
        elif tag.strip().startswith("PROPN"):
            worddict["PROPN"].append(word.strip())
        elif tag.strip().startswith("PRON"):
            worddict["PRON"].append(word.strip())
for key in worddict:
    worddict[key] = list(set(worddict[key]))

print worddict["PRON"]
with open('wordlists_'+sys.argv[1].split('.')[0]+'.txt', 'w') as outfile:
    json.dump(worddict, outfile)
