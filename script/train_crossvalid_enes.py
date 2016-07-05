#!/usr/bin/python
# -*- coding: utf-8 -*-

#usage python train_crossvalid.py folder_with_sets

import sys
import os
import subprocess
setfolder=sys.argv[1]
setnr=10
for i in range(setnr):
   p= subprocess.Popen(['python','run.py','-f',setfolder+'/set'+str(i)+'/train','-t', '../tree_tagger/cmd/tree-tagger-english','-d','../tree_tagger/cmd/tree-tagger-spanish','-c','../../../../tools/CRF++-0.58','-r', '-w','../wordlists/wordlists_eng-ud-all.txt','-v','../wordlists/wordlists_es-ud-all.txt','--model_lid',setfolder+'/set'+str(i)+'/crf_model_language_detection','--model_pos',setfolder+'/set'+str(i)+'/crf_model_pos'])
   p.communicate()

