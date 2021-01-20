import numpy as np
import pandas as pd


def entropy(class0, class1,class2):
    particle0 = particle1 = particle2 = 0
    if class0:
           particle0 = class0 * np.log2(class0)
    if class1:
           particle1 = class1 * np.log2(class1)
    if class2:
           particle1 = class2 * np.log2(class2)
           
    return (-(particle0 + particle1 + particle2 ))


df = pd.read_excel('detaFruit.xlsx')[['class', 'attr1', 'attr2', 'attr3']]
print(df.head())
print(df.describe())

s1_class0 = 0
s1_class1 = 0
s1_class2 = 0

#total number of fruits
total = len(df)


for i,row in df.iterrows():
    if row['class'] =='melon' :
        s1_class0 = s1_class0 + 1
    elif row['class'] =='orange' :
        s1_class1 = s1_class1 + 1
    elif row['class'] =='apple' :
        s1_class2 = s1_class2 + 1
    
s_entropy = entropy(s1_class0/total, s1_class1/total, s1_class2/total)
print('Dataset Entropy: %.3f bits' % s_entropy)

c1_class0 = 0
c1_class1 = 0
c1_class2 = 0

#total number of fruits
total = len(df)
# conditionVaue = 223
# attrib = 'attr3'
attribs = ['attr1', 'attr2', 'attr3']
bestCondition = ['', 0, 0]
for attr in attribs:
    a25 = df.describe().loc['25%'][attr]
    a75 = df.describe().loc['75%'][attr]
    for number in range(int(a25), int(a75)):
        conditionVaue = number
        attrib = attr
        c1_class0 = c1_class1 = c1_class2 = 0
        for i,row in df.iterrows():
            if row['class'] =='melon' and row[attrib] < conditionVaue :
                c1_class0 = c1_class0 + 1
            elif row['class'] =='orange' and row[attrib] < conditionVaue:
                c1_class1 = c1_class1 + 1
            elif row['class'] =='apple'  and row[attrib] < conditionVaue:
                c1_class2 = c1_class2 + 1
        c1_total = c1_class0 + c1_class1 + c1_class2
        c1_entropy = entropy(c1_class0/c1_total , c1_class1/c1_total , c1_class2/c1_total )

        dc1_class0 = 0
        dc1_class1 = 0
        dc1_class2 = 0

        for i,row in df.iterrows():
            if row['class'] =='melon' and row[attrib] >= conditionVaue :
                dc1_class0 = dc1_class0 + 1
            elif row['class'] =='orange' and row[attrib] >= conditionVaue:
                dc1_class1 = dc1_class1 + 1
            elif row['class'] =='apple'  and row[attrib] >= conditionVaue:
                dc1_class2 = dc1_class2 + 1
        dc1_total = dc1_class0 + dc1_class1 + dc1_class2
        dc1_entropy = entropy(dc1_class0/dc1_total , dc1_class1/dc1_total , dc1_class2/dc1_total )

        conditionEntropy = (c1_total / total) * c1_entropy + (dc1_total/total) * dc1_entropy
        # print('Condition Entropy: %.3f bits' % conditionEntropy)

        gain = s_entropy - conditionEntropy
        # print('Information Gain: %.3f bits' % gain)
        print("%.3f"%gain)
        if gain > bestCondition[2]:
            bestCondition[0] = attrib
            bestCondition[1] = conditionVaue
            bestCondition[2] = gain
print(bestCondition)
