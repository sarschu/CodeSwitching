#!/usr/bin/env python

# -*- coding: utf-8 -*-
#usage python eval_language_detection.py folder_with_sets taggedfile mode(test/dev)
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

acc=[]
baseline_acc_l=[]
baseline_acc_e=[]
baseline_acc_a=[]
baseline_acc_n=[]
baseline_acc_p=[]
l ={'l':0,'e':0,'a':0,'p':0,'n':0}
a ={'l':0,'e':0,'a':0,'p':0,'n':0}
n ={'l':0,'e':0,'a':0,'p':0,'n':0}
p ={'l':0,'e':0,'a':0,'p':0,'n':0}
e ={'l':0,'e':0,'a':0,'p':0,'n':0}
VERB ={'VERB':0,'NOUN':0,'PRON':0,'ADJ':0,'ADV':0,'ADP':0,'CONJ':0,'DET':0,'NUM':0,'PRT':0,'X':0,'PUNCT':0}
NOUN ={'VERB':0,'NOUN':0,'PRON':0,'ADJ':0,'ADV':0,'ADP':0,'CONJ':0,'DET':0,'NUM':0,'PRT':0,'X':0,'PUNCT':0}
PRON ={'VERB':0,'NOUN':0,'PRON':0,'ADJ':0,'ADV':0,'ADP':0,'CONJ':0,'DET':0,'NUM':0,'PRT':0,'X':0,'PUNCT':0}
ADJ={'VERB':0,'NOUN':0,'PRON':0,'ADJ':0,'ADV':0,'ADP':0,'CONJ':0,'DET':0,'NUM':0,'PRT':0,'X':0,'PUNCT':0}
ADV={'VERB':0,'NOUN':0,'PRON':0,'ADJ':0,'ADV':0,'ADP':0,'CONJ':0,'DET':0,'NUM':0,'PRT':0,'X':0,'PUNCT':0}
ADP ={'VERB':0,'NOUN':0,'PRON':0,'ADJ':0,'ADV':0,'ADP':0,'CONJ':0,'DET':0,'NUM':0,'PRT':0,'X':0,'PUNCT':0}
CONJ ={'VERB':0,'NOUN':0,'PRON':0,'ADJ':0,'ADV':0,'ADP':0,'CONJ':0,'DET':0,'NUM':0,'PRT':0,'X':0,'PUNCT':0}
DET={'VERB':0,'NOUN':0,'PRON':0,'ADJ':0,'ADV':0,'ADP':0,'CONJ':0,'DET':0,'NUM':0,'PRT':0,'X':0,'PUNCT':0}
NUM={'VERB':0,'NOUN':0,'PRON':0,'ADJ':0,'ADV':0,'ADP':0,'CONJ':0,'DET':0,'NUM':0,'PRT':0,'X':0,'PUNCT':0}
PRT ={'VERB':0,'NOUN':0,'PRON':0,'ADJ':0,'ADV':0,'ADP':0,'CONJ':0,'DET':0,'NUM':0,'PRT':0,'X':0,'PUNCT':0}
X ={'VERB':0,'NOUN':0,'PRON':0,'ADJ':0,'ADV':0,'ADP':0,'CONJ':0,'DET':0,'NUM':0,'PRT':0,'X':0,'PUNCT':0}
PUNCT ={'VERB':0,'NOUN':0,'PRON':0,'ADJ':0,'ADV':0,'ADP':0,'CONJ':0,'DET':0,'NUM':0,'PRT':0,'X':0,'PUNCT':0}
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

            word,lang,pos=line.strip().split('\t')

            if word != gold['WORD'][index]:
                print line
                print gold['WORD'][index]
                sys.exit()
            if gold['POS'][index] == u'.':
                toexec='posvar = '+'PUNCT'
            else:
                toexec = 'posvar = ' + gold['POS'][index]
            exec(toexec)
            if pos == u'.':
                posvar['PUNCT']+=1
            else: posvar[pos]+=1
            if (gold['POS'][index]=='NOUN' and pos == 'ADJ'):
                if gold['LID'][index]=='e':
                    engl+=1
                else:
                    lat+=1

            toexec2 = 'lidvar = ' + gold['LID'][index]
            if gold['LID'][index] =='p' and lang !='p':
                print i
                print word
                print lang
            exec(toexec2)
            lidvar[lang]+=1

            

                
#            if lang==gold['LID'][index]:
#                if lang.strip() =='l':

#                    l['l']+=1
#                if lang.strip() =='e':
#                    e['e']+=1
#                if lang.strip() =='p':
#                    p['p']+=1
#                if lang.strip() =='n':
#                    n['n']+=1
#                if lang.strip() =='a':
#                    a['a']+=1
#                corr+=1
#            else:
#                incorrect+=1
#                if gold['LID'][index].strip() in ['e','l']:
#                    ic_l+=1
#                if gold['LID'][index].strip() =='e':
#                    if lang =='l':
#                        e['l']+=1
#                    if lang =='p':
#                        e['p']+=1
#                    if lang =='a':
#                        e['a']+=1
#                    if lang =='n':
#                        e['n']+=1
#                if gold['LID'][index].strip() =='l':
#                    if lang =='e':
#                        l['e']+=1
#                    if lang =='p':
#                        l['p']+=1
#                    if lang =='a':
#                        l['a']+=1
#                    if lang =='n':
#                        l['n']+=1
#                if gold['LID'][index].strip() =='n':
#                    if lang =='l':
#                        n['l']+=1
#                    if lang =='p':
#                        n['p']+=1
#                    if lang =='a':
#                        n['a']+=1
#                    if lang =='e':
#                        n['e']+=1
#                    ic_n+=1
#                if gold['LID'][index].strip() =='a':
#                    if lang =='l':
#                        n['l']+=1
#                    if lang =='p':
#                        n['p']+=1
#                    if lang =='n':
#                        n['n']+=1
#                    if lang =='e':
#                        n['e']+=1
#                    ic_a+=1
#                if gold['LID'][index].strip() =='p':
#                    if lang =='l':
#                        print i
#                        print ls
#                        p['l']+=1
#                    if lang =='a':
#                        p['a']+=1
#                    if lang =='n':
#                        p['n']+=1
#                    if lang =='e':
#                        p['e']+=1
#                    ic_p+=1

#            if gold['LID'][index].strip() == 'l':
#                corr_bl+=1
#            if gold['LID'][index].strip() == 'e':
#                corr_be+=1
#            if gold['LID'][index].strip() == 'a':
#                corr_ba+=1
#            if gold['LID'][index].strip() == 'p':
#                corr_bp+=1
#            if gold['LID'][index].strip() == 'n':
#                corr_bn+=1
            index+=1
#    print corr
#    print len(crf_test)
#    dist_ic_l.append(float(ic_l)/incorrect)
#    dist_ic_a.append(float(ic_a)/incorrect)
#    dist_ic_n.append(float(ic_n)/incorrect)
#    acc.append(float(corr)/len(crf_test))
#    baseline_acc_l.append(float(corr_bl)/len(crf_test))
#    baseline_acc_e.append(float(corr_be)/len(crf_test))
#    baseline_acc_a.append(float(corr_ba)/len(crf_test))
#    baseline_acc_p.append(float(corr_bp)/len(crf_test))
#    baseline_acc_n.append(float(corr_bn)/len(crf_test))
#print acc
#print baseline_acc_l
#print  baseline_acc_e
#print 'average acc'
#print sum(acc)/setnr
#print 'average acc_l'
#print sum(baseline_acc_l)/setnr
#print 'average acc_e'
#print sum(baseline_acc_e)/setnr
#print 'average acc_p'
#print sum(baseline_acc_p)/setnr
#print 'average acc_a'
#print sum(baseline_acc_a)/setnr
#print 'average acc_n'
#print sum(baseline_acc_n)/setnr
#print 'average nr incorrect lang'
#print sum(dist_ic_l)/setnr
#print 'average nr incorrect n'
#print sum(dist_ic_n)/setnr
#print 'average nr incorrect a'
#print sum(dist_ic_a)/setnr
p_a_l=0.
r_a_l=0.
f_a_l=0.
for lid_label in ['l','e','a','p','n']:
    FP=0.0
    TP=0.0
    FN=0.0
    print lid_label
    toexec2 = 'lidvar = ' + lid_label
    exec(toexec2)
    print lidvar
    TP= lidvar[lid_label]
    for lab in ['l','e','a','p','n']:
        if lab == lid_label:
            pass
        else:
            toexec = 'lid = ' + lab
            exec(toexec)
            print lid['l']
            FP+=lid[lid_label]
            FN+=lidvar[lab]
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
for pos_label in ['ADJ','ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM', 'PRON', 'PRT', 'VERB', 'X', 'PUNCT']:
    FP=0.0
    TP=0.0
    FN=0.0
    print pos_label
    if pos_label == '.':
        toexec2 = 'posvar = PUNCT'
    else:
        toexec2 = 'posvar = ' + pos_label
    exec(toexec2)
    print posvar
    TP= posvar[pos_label]
    for lab in ['ADV','ADP', 'DET', 'VERB', 'X', 'CONJ', 'ADJ', 'NOUN', 'PRT', 'PUNCT', 'PRON', 'NUM']:
        if lab == pos_label:
            pass
        else:

            if lab == '.':
                toexec = 'pos = PUNCT'
            else:
                toexec = 'pos= ' + lab

            exec(toexec)
            FP+=pos[pos_label]
            FN+=posvar[lab]
    sum_a=0.
    for k in posvar:
        if k != pos_label:
            sum_a+= posvar[k]
    print 'percentage of error:'
    print 100.- (100./(sum_a+TP))*TP
    for k in posvar: 
        print k 
        print (100/sum_a)*posvar[k]
    print '\n'
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
print r_a_l/5
print 'overall precision'
print p_a_l/5
print 'overall f'
print f_a_l/5

print 'precs'
print ' & '.join([str(x) for x in precs])
print 'recs'
print ' & '.join([str(x) for x in recs])
print 'fscores'
print ' & '.join([str(x) for x in fscores])

print 'pos'
print 'overall recall'
print r_a/12
print 'overall precision'
print p_a/12
print 'overall f'
print f_a/12
