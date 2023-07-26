# TreeInvent-Community
SVC_QSAR_Models provides SVC QSAR models for all the target with more than 1000 active ligand datas in the public ESCAPE-DB datasets.
## Description
This respositories contains all the SVC models and its accuracy on the target in ESCAPE-DB with more than 1000 active datas. For each model, all the active datas and the same number of inactives are used as our datasets. And the dataset is splited into training set and test set with the ratio of 0.9:0.1. The accuracy of SVC models are evaluated on the test sets. These models can be used as scoring function in Tree-Invent's RL-algorithm for ligand based molecular generation.
## QSAR Accuracy 
|Uniprot Code| Accuracy on Test set|
|------------|---------------------|
|ACHE        |  0.864              |
|ADAM17      |  0.996              |
|ADRB2       |  0.847              |
|AKT1        |  0.950              |
|ALOX15B     |  0.723              |
|ALOX15      |  0.712              |
|APOBEC3F    |  0.670              |
|APOBEC3G    |  0.772              |
|AR          |  0.912              |
|ATM         |  0.566              |
|AVPR1A      |  0.985              |
|BAZ2B       |  0.614              |
|CASP1       |  0.905              |
|CASP3       |  0.890              |
|CASP7       |  0.901              |
|CBX1        |  0.604              |
|CHRM1       |  0.938              |
|CLK4        |  0.911              |
|CTSL        |  0.968              |
|CTSS        |  0.990              |
|CYP19A1     |  0.944              |
|CYP1A2      |  0.708              |
|CYP2C19     |  0.768              |
|CYP2C9      |  0.752              |
|CYP2D6      |  0.748              |
|DRD1        |  0.909              |
|DRD2        |  0.988              |
|DRD3        |  0.981              |
|DYRK1A      |  0.919              |
|EPHX2       |  0.980              |
|ERG         |  0.623              |
|ESR1        |  0.920              |
|ESR2        |  0.932              |
|F2          |  0.978              |
|FEN1        |  0.719              |
|GAA         |  0.639              |
|GBA         |  0.634              |
|GFER        |  0.830              |
|GLS         |  0.680              |
|GSK3A       |  0.871              |
|GSK3B       |  0.934              |
|HIF1A       |  0.721              |
|HPGD        |  0.770              |
|HSD17B10    |  0.617              |
|HSP90AA1    |  0.819              |
|HTR1A       |  0.989              |
|HTR2A       |  0.961              |
|IDH1        |  0.730              |
|JAK2        |  0.929              |
|KAT2A       |  0.561              |
|KCNH2       |  0.938              |
|KDM4A       |  0.706              |
|KDM4E       |  0.619              |
|KMT2A       |  0.605              |
|L3MBTL1     |  0.548              |
|MAOA        |  0.751              |
|MAP4K2      |  0.915              |
|MAPK1       |  0.641              |
|MC4R        |  0.992              |
|MCHR1       |  0.964              |
|MCL1        |  0.846              |
|MMP13       |  0.974              |
|MMP2        |  0.962              |
|MTOR        |  0.833              |
|NPSR1       |  0.704              |
|NR3C1       |  0.922              |
|OPRK1       |  0.975              |
|OPRM1       |  0.966              |
|PAX8        |  0.853              |
|PIN1        |  0.677              |
|PKM         |  0.674              |
|PLK1        |  0.806              |
|POLB        |  0.598              |
|POLH        |  0.782              |
|POLI        |  0.624              |
|PPARA       |  0.940              |
|PPARD       |  0.937              |
|PPARG       |  0.949              |
|PRKACA      |  0.956              |
|PTK2        |  0.904              |
|PTPN1       |  0.833              |
|RECQL       |  0.583              |
|ROCK2       |  0.957              |
|S1PR1       |  0.985              |
|SLC6A3      |  0.972              |
|SMN2        |  0.811              |
|SNCA        |  0.669              |
|THRB        |  0.689              |
|TRPC4       |  0.801              |
|TRPV1       |  0.939              |
|TSHR        |  0.673              |
|TXNRD1      |  0.622              |
|USP2        |  0.741              |
|VDR         |  0.739              |

## Dependency
Tree-Invent (https://github.com/MingyuanXu/Tree-Invent)

## Files
all the activity data are zipped in csv.zip, which could be uncompressed with the command of "tar -xvf csv.zip".  

SVC QSAR model are zipped in activity.tar.gz, which could also be uncompressed with the command of "tar -xvf activity.tar.gz". This model can be directly loaded into Tree-Invent for drug designs.  

qsar.py are used the create this SVC model.  

evaluate.py are used to evaluate the SVC model.  

all the datas are stored in Google Drive (https://drive.google.com/drive/folders/1i2OUGKSFDjP82a5D0CCp-ekpHZaQuceI?usp=sharing)

## Contributors:
[@Mingyuan Xu](https://github.com/MingyuanXu)

