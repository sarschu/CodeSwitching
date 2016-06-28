#!/usr/bin/python
# -*- coding: utf-8 -*-

# usage: PosTag.py infile train(True,False) model_l model_pos 

import datetime
import os
import sys
import subprocess
from preprocess_input import Preprocess
from make_feature_file import MFF_Lang_Detection
from make_feature_file_POS import MFF_Pos
import nltk.tokenize
import time
import codecs

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
class Tagger:

    def __init__(self,filename=None,training=False,model_lid='../models/language_detection_model'+st,model_pos='../models/pos_model'+st,template_lid='../models/template_lid',template_pos='../models/template_pos',crf='/usr/local/bin',treetagger_l1='../tree_tagger/cmd/tree-tagger-middleenglish',treetagger_l2='../tree_tagger/cmd/tree-tagger-latin',wordlist1="../wordlists/wordlists_lat.txt",wordlist2="../wordlists/wordlists.txt"):
        infile = os.path.abspath(filename)
        self.infile=infile
        self.crf= crf
        self.wordlist= wordlist1
        self.wordlist2 = wordlist2

        self.train=training
        self.inf = infile+'.tok'
        self.treetagger_l1 = treetagger_l1
        print self.treetagger_l1
        self.treetagger_l2 = treetagger_l2
        if self.train:
            os.system("cut -f1 -d'\t' "+self.infile+" > "+self.inf)
        else:
            self.inf_text=filename
            out = codecs.open(self.inf,'w','utf8')
            text = codecs.open(self.inf_text,'r','utf8').read()
            text = nltk.word_tokenize(text)
            for tok in text:
                out.write(tok+'\n')
            out.close()
        
        if self.train ==True:
            self.template_lid=os.path.abspath(template_lid)
            self.template_pos=os.path.abspath(template_pos)


        self.model_l= os.path.abspath(model_lid)
        self.model_pos= os.path.abspath(model_pos)

    def run(self):
        prepro= Preprocess(self.inf,self.treetagger_l1,self.treetagger_l2)

        l1_tt = prepro.tree_tag_l1()
        l2_tt = prepro.tree_tag_l2()
        mff_ld=MFF_Lang_Detection()
        
        # in case we are in training mode, make the feature files with gold label
        if self.train:

            ff_ld= mff_ld.mff(self.infile,l1_tt, l2_tt,self.train,self.wordlist, self.wordlist2)
        # in case we are not in training mode, make the feature files ohne gold label
        else:
            ff_ld= mff_ld.mff(self.inf,l1_tt, l2_tt,self.train,self.wordlist, self.wordlist2)

        #in case we are in training mode, train crf
        if self.train == True:
          
            crf_learn = subprocess.Popen([self.crf+'/crf_learn','-p','4','-c','1000.',self.template_lid,ff_ld,self.model_l])
            out,err = crf_learn.communicate()
        # in case we are not in training mode run crf
        if self.train ==False:
            ff_pos = ff_ld[:-4]+'.pos.features'

            ff_pos_file = codecs.open(ff_ld[:-4]+'.pos.features','w','utf8')
            
            crf_test = subprocess.Popen([self.crf+'/crf_test','-m',self.model_l,ff_ld],stdout=ff_pos_file)
            o,e=crf_test.communicate()
            ff_pos_file.close()

        else:
            mff_pos=MFF_Pos()
            
            ff_pos= mff_pos.mff(self.infile,ff_ld, self.train)

        if self.train ==True:
            
            crf_learn = subprocess.Popen([self.crf+'/crf_learn','-p','4','-c','1000.',self.template_pos,ff_pos,self.model_pos])
            out,err = crf_learn.communicate()

        if self.train != True:
            outfile = self.infile+'.pos_tmp'
            out = codecs.open(outfile,'w','utf8')

            crf_test = subprocess.Popen([self.crf+'/crf_test','-m',self.model_pos,ff_pos],stdout=out)
            crf_test.communicate()
            out.close()
            withfeat = codecs.open(outfile,'r','utf8').readlines()
            outfilename = self.infile+'.pos_tagged'
            out_final = codecs.open(outfilename,'w','utf8')
            idn=1
            for line in withfeat:
                if line.strip() != '':
                    out_final.write(str(idn)+'\t'+line.split()[0]+'\t'+line.split()[-2]+'\t_\t'+line.split()[-1].strip()+'\t_\t_\t_\t_\t_\t_\t_\t_\t_\t_\n')
                    #idn+=1
                    #out_final.write(line.split()[0]+'\t'+line.split()[-2]+'\t'+line.split()[-1].strip()+'\n')
                else:
                    out_final.write('\n')
                    idn=0
            out_final.close()

