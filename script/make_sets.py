import sys
import codecs
import random
import json
from math import ceil
import os

# usage: python make_sets.py feature_file

all_toks=codecs.open(sys.argv[1],'r','utf8').readlines()



setnr=10
myList=[i for i in range(len(all_toks))]
N=len(all_toks)
for i in range(setnr):
	os.system('mkdir set'+str(i))
        index_dict={'train':[],'test':[],'dev':[]}
        test_f= codecs.open('set'+str(i)+'/test','w','utf8')
        dev_f= codecs.open('set'+str(i)+'/dev','w','utf8')
        train_f= codecs.open('set'+str(i)+'/train','w','utf8')
        start = (N / setnr) * i
        T = int(ceil(0.8 * N))
        tmpN = N - T
        D  = int(ceil(0.5 * tmpN))
        TE = int(N - (T + D))
        s_train = int(start)
        e_train = int((s_train + T) % N)
        s_dev = int(e_train)
        e_dev = int((s_dev + D) % N)
        s_test = int(e_dev)
        e_test = int((s_test + TE) % N)

        if(e_train > s_train):
            index_dict['train'] = myList[s_train:e_train]
        else:
            index_dict['train'] = myList[:e_train] + myList[s_train:]

        if(e_dev > s_dev):
            index_dict['dev'] = myList[s_dev:e_dev]
        else:
            index_dict['dev'] = myList[:e_dev] + myList[s_dev:]

        if(e_test > s_test):
            index_dict['test'] = myList[s_test:e_test]
        else:
            index_dict['test'] = myList[:e_test] + myList[s_test:]

        for index in index_dict['train']:
            train_f.write(all_toks[index])
	for index in index_dict['dev']:
            dev_f.write(all_toks[index])
        for index in index_dict['test']:
	    test_f.write(all_toks[index])
	jsfile = open('set'+str(i)+'/indices.json', 'w')
	json.dump(index_dict,jsfile)
	jsfile.close()
	test_f.close()
	train_f.close()
	dev_f.close()

	
