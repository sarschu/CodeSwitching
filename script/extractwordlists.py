#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import json
import sys

ppcme = codecs.open(sys.argv[1],'r','utf8').read()

ppcme_toks = ppcme.split()


worddict={'ADJ':[],'ADP':[],'ADV':[],'AUX':[],'CONJ':[],'DET':[],'INTJ':[],'PROPN':[],"NOUN":[],'PRON':[],'PROPN':[],'VERB':[]}

for el in ppcme_toks:
    if '/' in el:
        word,tag=el.split('/')
        if tag.strip().startswith('ADJ'):
            worddict["ADJ"].append(word.strip())
        elif tag.strip().startswith("ADV") or tag.strip().startswith("WADV"):
            worddict["ADV"].append(word.strip())
        elif  tag.strip().startswith("V"):
            worddict["VERB"].append(word.strip())
        elif tag.strip().startswith("B") or tag.strip().startswith("DA") or tag.strip().startswith("DO") or tag.strip().startswith("H"):
            worddict["AUX"].append(word.strip())
        elif tag.strip()== "P":
            worddict["ADP"].append(word.strip())
        elif tag.strip()== "CONJ":
            worddict["CONJ"].append(word.strip())
        elif tag.strip()== "D":
            worddict["DET"].append(word.strip())
        elif tag.strip()=='INTJ':
            worddict["INTJ"].append(word.strip())
        elif tag.strip()== "N" or  tag.strip()== "N$":
            worddict["NOUN"].append(word.strip())
        elif tag.strip().startswith("NPR"):
            worddict["PROPN"].append(word.strip())
        elif tag.strip().startswith("PRO"):
            worddict["PRON"].append(word.strip())
for key in worddict:
    worddict[key] = list(set(worddict[key]))

print worddict["PRON"]
with open('wordlists_me.txt', 'w') as outfile:
    json.dump(worddict, outfile)
