#!/usr/bin/python
# -*- coding: utf-8 -*-

#usage python preprocess_input.py tok_file

#features char n grams
#pos middleenglish tagger
#prob middleenglish tagger
#pos latin tagger
#prob latin tagger

import sys
import re
import subprocess
import codecs
import os

class Preprocess:

    def __init__(self, inf,ttl1,ttl2):
        self.ttl1 = ttl1
        self.ttl2=ttl2
        self.inf = inf


    def tree_tag_l1(self):
        inp=codecs.open(self.inf,'r','utf8')
        #me_out=codecs.open('.'.join(sys.argv[1].split('.')[:-1])+'.eng','w','utf8')
        print self.inf
        print self.ttl1
        print os.path.abspath('/'.join(self.ttl1.split('/')[:-2]))
        me_out=codecs.open('.'.join(self.inf.split('.')[:-1])+'.l1','w','utf8')
        mt= subprocess.Popen([self.ttl1,'/'.join(self.ttl1.split('/')[:-2])],stdin=inp,stdout=me_out)
        #mt= subprocess.Popen([absolpath+'/../tree_tagger_files/tree-tagger-english',absolpath],stdin=inf,stdout=me_out)
        inp.close()
        out,err = mt.communicate()
        me_out.close()
        return os.path.abspath('.'.join(self.inf.split('.')[:-1])+'.l1')

    def tree_tag_l2(self):


        inp=codecs.open(self.inf,'r','utf8')
        lat_out=codecs.open('.'.join(self.inf.split('.')[:-1])+'.l2','w','utf8')
        #lat_out=codecs.open('.'.join(sys.argv[1].split('.')[:-1])+'.span','w','utf8')
        lt= subprocess.Popen([self.ttl2,'/'.join(self.ttl1.split('/')[:-2])],stdin=inp,stdout=lat_out)
        #lt= subprocess.Popen([absolpath+'/../tree_tagger_files/tree-tagger-spanish',absolpath],stdin=inf,stdout=lat_out)
        inp.close()
        out,err = lt.communicate()



        lat_out.close()
        return os.path.abspath('.'.join(self.inf.split('.')[:-1])+'.l2')
