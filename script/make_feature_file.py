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
import json

class MFF_Lang_Detection:

    def __init__(self):
        pass

    def ngr_suffix(self,word,n):
        return word[-n:]
    
    def ngr_prefix(self,word,n):
         return word[:n]
    
    def get_wordlists(self,word_dict, words):
     
        tlist=[]
        with open(word_dict) as json_file:
            json_data = json.load(json_file)
            for word in words:

                word = word.strip().split('\t')[0]

                appended=False
                for key in json_data:
                    #print json_data[key]
                    if word in json_data[key]:
                        tlist.append(key)
                        appended=True
                        break
                if appended ==False:
                     tlist.append('None')

        return tlist
        
        
    def extract_features(self,word,f_m,f_l,mode,w_l,w_me):

        #print all features
        #if len(g2) !=0 and len(g3)==0:
        features= word+"\t"+w_l+'\t'+w_me+'\t'+f_m+'\t'+f_l+"\t"+self.ngr_prefix(word,1)+"\t"+self.ngr_prefix(word,2)+'\t'+self.ngr_prefix(word,3)+'\t'+self.ngr_suffix(word,1)+'\t'+self.ngr_suffix(word,2)+'\t'+self.ngr_suffix(word,3)+'\t'+mode
        #elif len(g2) == 0:
        #    features= word+"\t"+self.get_wordlists(w_l,word)+'\t'+self.get_wordlists(w_me,word)+"\t"+f_m+'\t'+f_l+'\t'+word[-1]+"\t"+'\t'.join(['None' for x in range(m2-len(g2))])+'\t'+'\t'.join(['None' for x in range(m3-len(g3))])+'\t'+mode
        #else:
        #    features= word+"\t"+self.get_wordlists(w_l,word)+'\t'+self.get_wordlists(w_me,word)+"\t"+f_m+'\t'+f_l+'\t'+word[-1]+"\t"+'\t'.join(g2)+"\t"+'\t'.join(['None' for x in range(m2-len(g2))])+"\t"+'\t'.join(g3)+'\t'+'\t'.join(['None' for x in range(m3-len(g3))])+'\t'+mode
        return features.strip()+'\n'

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
            else:
                    f_d['0'].append('X')
                    f_d['1'].append('1.000000')
               
        return f_d

    def mff(self,toktext,me_tagged, lat_tagged,tvalue,wl1,wl2):

        text= codecs.open(toktext,'r','utf8').readlines()

      
        splitn= toktext.split('.')
        if len(splitn)>1:
            feature_file = codecs.open('.'.join(toktext.split('.')[:-1])+'.features',"w","utf8")
        else:
            feature_file = codecs.open(toktext+'.features',"w","utf8")
        
        md = codecs.open(me_tagged,'r','utf8')
        lat = codecs.open(lat_tagged,'r','utf8')
        train=tvalue
        if train!= True:
          
            train = False

        fd_1 = self.extract_pos_prob_list(md)
        print len(fd_1)
        print len(text)
        fd_2 = self.extract_pos_prob_list(lat)
        wl_1=self.get_wordlists(wl1,text)
        wl_2=self.get_wordlists(wl2,text)
        md.close()
        lat.close()
        mode=''

        w_c=0
        for i,w in enumerate(text):
                    
            if w == '' or w=='\n':
                feature_file.write('\n')
                continue
            
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
            feature_file.write(self.extract_features(re.sub('\_[leapn]','',w),f_1.strip(),f_2.strip(),mode,wl_1[i],wl_2[i]))
            if re.sub('\_[leapn]','',w) in [u'.',u'?',u'!']:

                feature_file.write('\n')

            

        feature_file.close()
       
        if len(splitn)>1:
            return '.'.join(toktext.split('.')[:-1])+'.features'
        else:
            return toktext+'.features'

