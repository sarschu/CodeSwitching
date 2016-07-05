#!/usr/bin/python
# -*- coding: utf-8 -*-


#usage make_feature_file_POS.py goldstandfile featurefile train[True,False]


#features char n grams
#pos middleenglish tagger
#prob middleenglish tagger
#pos latin tagger
#prob latin tagger

import sys
import re
import codecs

class MFF_Pos:
    def __init__(self):
        pass

    #1a 
    def ngr(self,text,n):
        ng = []
        for w in text:
            w = re.sub('\_[SE]','',w).strip()
            ng.append([w[i:i+n] for i in range(len(w)-n+1)])
        return ng
        


    def extract_features(self,word,pos_m,prob_m,pos_l,prob_l,mode,g2,m2,g3,m3):

        #print all features
        features= word+"\t"+str(pos_l)+"\t"+str(pos_m)+"\t"+str(prob_l)+ \
        "\t"+str(prob_m)+"\t"+'\t'.join(g2)+"\t"+'\t'.join(['None' for x in range(m2-len(g2))])+"\t"+'\t'.join(g3)+'\t'+'\t'.join(['None' for x in range(m3-len(g3))])+'\t'+mode

        return features.strip()+'\n'


    def extract_pos_prob_list(self,tagged):
        t_lines = tagged.readlines()
        pos,prob = [],[]
        for line in t_lines:
            sl=line.strip().split()

            if sl !=[]:
               pos.append(sl[0].strip())
               prob.append(sl[1].strip())
        return pos,prob

    def mff(self,gold_pos,ff_ld,tvalue):
        train = tvalue
        if train != True:
            train= False   
        if train:
            text_pos= codecs.open(gold_pos,'r','utf8').readlines()
        f_ld = codecs.open(ff_ld,'r','utf8').readlines()
        feature_file = codecs.open(ff_ld[:-4]+'.pos.features',"w","utf8")
        empty_line_ct=0
        poscount=0
        for i,line in enumerate(f_ld):

            if line.strip()=='':
                feature_file.write('\n')
                #empty_line_ct+=1
            else:

                #word,pos_m,prob_m,pos_l,prob_l,mode,2g,m2,3g,m3

                if train:
                    if text_pos[poscount].split('\t')[0].strip() != line.split()[0].strip():
                        print text_pos[poscount].split('\t')[0].strip()
                        print line.split()[0].strip()
                        sys.exit()
                        
                    feature_file.write(line.strip()+'\t'+text_pos[poscount].split('\t')[2].strip()+'\n')
                else:
                    feature_file.write(line.strip()+'\n')
                poscount+=1


        feature_file.close()
        return ff_ld[:-4]+'.pos.features'
        


