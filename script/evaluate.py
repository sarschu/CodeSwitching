#!/usr/bin/env python

# -*- coding: utf-8 -*-
#usage python evaluate.py folder_with_sets taggedfile goldfile tagset_lang tagset_pos

#tagset should be a file with one tag per line

import codecs
import os
import re
import sys


setnr=10
inputfolder= sys.argv[1]
predicted_file=sys.argv[2]

precs=[]
recs=[]
fscores=[]

tagset_l= [x.strip() for x in codecs.open(sys.argv[4],'r','utf8').readlines()]
tagset_pos= [x.strip() for x in codecs.open(sys.argv[5],'r','utf8').readlines()]

l_dict={}
pos_dict={}

for l in tagset_l:
    l_dict[str(l)]={}
    for t in tagset_l:
        l_dict[str(l)][str(t)]=0.
        
   
for l in tagset_pos:
    pos_dict[str(l)]={}
    for t in tagset_pos:
        pos_dict[str(l)][str(t)]=0.
        
print pos_dict
dist_ic_l=[]
dist_ic_n=[]
dist_ic_a=[]
engl=0
lat=0
engl2=0
lat2=0
for i in range(setnr):
    corr=0
    corr_bl=0
    corr_be=0
    corr_ba=0
    corr_bp=0
    corr_bn=0
    incorrect=0
    ic_l=0
    ic_n=0
    ic_a=0

    ic_p=0
    gold_t= codecs.open(inputfolder+'/set'+str(i)+'/'+sys.argv[3],'r','utf8').readlines()
    gold = {'POS':[],'LID':[],'WORD':[]}
    for line in gold_t:
        gold['POS'].append(line.split('\t')[2].strip())
        gold['LID'].append(line.split('\t')[1].strip())
        gold['WORD'].append(line.split('\t')[0].strip())
    crf_test = codecs.open(inputfolder+'/set'+str(i)+'/'+predicted_file,'r','utf8').readlines()
    index=0

    for line in crf_test:
        if line.strip()!='':
            ls=line.strip().split('\t')
            word,lang,pos=ls[1],ls[2],ls[4]

            if word != gold['WORD'][index]:
                print line
                print gold['WORD'][index]
                sys.exit()
          
            pos_dict[pos][gold['POS'][index]]+=1
            l_dict[lang][gold['LID'][index]]+=1

            index+=1

p_a_l=0.
r_a_l=0.
f_a_l=0.
for lid_label in tagset_l:
    FP=0.0
    TP=0.0
    FN=0.0
    TP= l_dict[lid_label][lid_label]
    for lab in tagset_l:
        if lab == lid_label:
            pass
        else:
            FP+=l_dict[lab][lid_label]
            FN+=l_dict[lid_label][lab]
    print l_dict[lid_label]
    print lid_label
    print 'Precision'
    if TP+FP==0.0: 
        pre = 0.0
    else:
        pre=TP/(TP+FP)
    p_a_l+=pre
    print pre
    if TP+FN ==0.0:
        re=0.0
    else:
        re=TP/(TP+FN)
    print 'Recall'
    print re
    r_a_l+=re
    print 'F-score'
    if pre ==0.0 or re == 0.0:
        f = 0.0
    else:
        f= 2*(pre*re)/(pre+re) 
    print f
    f_a_l+=f

p_a=0.
r_a=0.
f_a=0.
for pos_label in tagset_pos:
    print pos_dict[pos_label]
    print pos_label
    FP=0.0
    TP=0.0
    FN=0.0
    TP= pos_dict[pos_label][pos_label]
    for pos in tagset_pos:
        if pos == pos_label:
            pass
        else:
            FP+=pos_dict[pos][pos_label]
            FN+=pos_dict[pos_label][pos]
    sum_a=0.
    for k in pos_dict[pos_label]:
        if k != pos_label:
            sum_a+= pos_dict[pos_label][k]
    
    print 'percentage of error:'
    if sum_a !=0.:
        print 100.- (100./(sum_a+TP))*TP
    
        for k in pos_dict[pos_label]: 
            print k 
            print (100/sum_a)*pos_dict[pos_label][k]
        print '\n'
    else:
        print 'no error'
    print 'Precision'
    if TP+FP==0.0: 
        pre = 0.0
        precs.append(pre)
    else:
        pre=TP/(TP+FP) 
        precs.append(pre)
    p_a+=pre
    print pre
    if TP+FN ==0.0:
        re=0.0
        recs.append(re)
    else:
        re=TP/(TP+FN)
        recs.append(re)
    r_a+=re
    print 'all'
    print TP+FN
    print 'Recall'
    print re
    print 'F-score'
    if pre ==0.0 or re == 0.0:
        f = 0.0
        fscores.append(f)
    else:
        f= 2*(pre*re)/(pre+re)
        fscores.append(f) 
    f_a+=f
    print f

print engl
print lat

print 'lid'
print 'overall recall'
print r_a_l/len(tagset_l)
print 'overall precision'
print p_a_l/len(tagset_l)
print 'overall f'
print f_a_l/len(tagset_l)

print 'precs'
print ' & '.join([str(x) for x in precs])
print 'recs'
print ' & '.join([str(x) for x in recs])
print 'fscores'
print ' & '.join([str(x) for x in fscores])

print 'pos'
print 'overall recall'
print r_a/len(tagset_pos)
print 'overall precision'
print p_a/len(tagset_pos)
print 'overall f'
print f_a/len(tagset_pos)
