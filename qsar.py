import torch
from FBG_3DGen.model import * 
from FBG_3DGen.comparm import * 
import argparse as arg
import pickle,os
import random 
import argparse as arg

parser=arg.ArgumentParser(description='SVC QSAR Model')
parser.add_argument('-i','--input')
args=parser.parse_args()
target=args.input

activelines=[]
inactivelines=[]
with open(f"{target}.dat",'r') as f:
    for line in f.readlines():
        var=line.split()
        if var[3]=='A':
            activelines.append(line)
        else:
            inactivelines.append(line)
with open(target+'_active.csv','w') as f:
    for line in activelines:
        f.write(line)
with open(target+'_inactive.csv','w') as f:
    for line in inactivelines:
        f.write(line)

smis1,labels1=deal_activity_csv(f'{target}_active.csv')
smis2,labels2=deal_activity_csv(f'{target}_inactive.csv')
ids=random.sample(list(np.arange(len(smis2))),min(len(smis2),len(smis1)))
smis2=[smis2[idx] for idx in ids]
labels2=[labels2[idx] for idx in ids]
smis=smis1+smis2
labels=labels1+labels2
#print (labels)
create_activity_model(smis,labels)
