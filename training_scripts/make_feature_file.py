#!/usr/bin/python
# -*- coding: utf-8 -*-

#usage python make_feature_file.py tokfile[/ldfile] treetagger1 treetagger2 train_mode[True,False]

#features char n grams
#pos middleenglish tagger
#prob middleenglish tagger
#pos latin tagger
#prob latin tagger

import sys
import re
import codecs

class MFF_Lang_Detection:

    def __init__(self):
        pass

    def ngr(self,text,n):
        ng = []
        for w in text:
            w = re.sub('\_[leapn]','',w).strip()
            ng.append([w[i:i+n] for i in range(len(w)-n+1)])
        return ng

    def extract_features(self,word,f_m,f_l,mode,g2,m2,g3,m3):

        #print all features
        if len(g2) !=0 and len(g3)==0:
            features= word+"\t"+f_m+'\t'+f_l+"\t"+'\t'.join(g2)+'\t'+'\t'.join(['None' for x in range(m2-len(g2))])+'\t'+'\t'.join(['None' for x in range(m3-len(g3))])+'\t'+mode
        elif len(g2) == 0:
            features= word+"\t"+f_m+'\t'+f_l+"\t"+'\t'.join(['None' for x in range(m2-len(g2))])+'\t'+'\t'.join(['None' for x in range(m3-len(g3))])+'\t'+mode
        else:
            features= word+"\t"+f_m+'\t'+f_l+"\t"+'\t'.join(g2)+"\t"+'\t'.join(['None' for x in range(m2-len(g2))])+"\t"+'\t'.join(g3)+'\t'+'\t'.join(['None' for x in range(m3-len(g3))])+'\t'+mode
        return features.strip()+'\n'
        print len(features.strip('\t').split('\t'))

    def extract_pos_prob_list(self,tagged):
        t_lines = tagged.readlines()
        
        pos,prob = [],[]
        f_d={}
        for p in range(len(t_lines[0].strip().split())):
        	f_d[str(p)]=[]
        print str(len(f_d)) +' features found\n'
        	
        for line in t_lines:
            sl=unicode(line).strip().split()
			
            if sl !=[]:
            	  for i in range(len(f_d)):

               		f_d[str(i)].append(sl[i].strip())
               
        return f_d

    def mff(self,toktext,me_tagged, lat_tagged,tvalue):

        text= codecs.open(toktext,'r','utf8').readlines()
        grams2 = self.ngr(text,2)
        grams3 = self.ngr(text,3)
        m2=40
        m3=30
        feature_file = codecs.open('.'.join(toktext.split('.')[:-1])+'.features',"w","utf8")
        md = codecs.open(me_tagged,'r','utf8')
        lat = codecs.open(lat_tagged,'r','utf8')
        train=tvalue
        if train!= True:
          
            train = False
        fd_1 = self.extract_pos_prob_list(md)
        fd_2 = self.extract_pos_prob_list(lat)
        md.close()
        lat.close()
        mode=''

        w_c=0
        for i,w in enumerate(text):
                    
            if w == '' or w=='\n':
                feature_file.write('\n')
                continue
            print w
            
            w=unicode(w)
            if train:
                w,l,p=w.strip().split()
                mode=l
               
            else:
                w = w.strip()
                mode=''

            f_1=''
            f_2=''


            for e in fd_1:
                f_1+=fd_1[e][w_c]+u'\t'
            for e in fd_2:
                f_2+=fd_2[e][w_c]+u'\t'
            w_c+=1
            #word,pos_m,prob_m,pos_l,prob_l,mode,2g,m2,3g,m3
            feature_file.write(self.extract_features(re.sub('\_[leapn]','',w),f_1.strip(),f_2.strip(),mode,grams2[i],m2,grams3[i],m3))
            if re.sub('\_[leapn]','',w) in [u'.',u'?',u'!']:

                feature_file.write('\n')

            

        feature_file.close()
        return '.'.join(toktext.split('.')[:-1])+'.features'
        

