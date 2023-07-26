import sklearn,math
import pickle 
from sklearn import svm,metrics
import numpy as np
with open('activity/SVC.pickle','rb') as f:
    model=pickle.load(f)
with open ('activity/X.pickle','rb') as f:
    X=pickle.load(f)
with open ('activity/Y.pickle','rb') as f:
    Y=pickle.load(f)

cut_rate=0.9
cutnum=math.ceil(len(X)*cut_rate)
#model.fit(np.array(X)[:cutnum],np.array(Y)[:cutnum])
scores=model.score(np.array(X)[cutnum:],np.array(Y)[cutnum:])
Y_pred=model.predict(np.array(X)[cutnum:])
s=metrics.roc_auc_score(np.array(Y)[cutnum:],Y_pred)
print (s)
