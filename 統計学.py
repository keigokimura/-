# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 18:49:56 2019

@author: 圭吾
"""

import numpy as np

#帰無仮設を棄却した回数
count=0

r=500
st=0
sa=0
se=0
x=0.117263

for j in range(100):

    #データ(正規分布に従う乱数)
    a1=np.random.normal(1/4,1,r);
    a2=np.random.normal(1/2,1,r);
    a3=np.random.normal(3/4,1,r);
    a4=np.random.normal(1,1,r);

    #各平均値
    m1=np.average(a1);
    m2=np.average(a2);
    m3=np.average(a3);
    m4=np.average(a4);

    #全体の平均
    m_all=(m1+m2+m3+m4)/4;

    #St計算
    for a in range(r):
        st+=pow(a1[a]-m_all,2)

    for b in range(r):
        st+=pow(a2[b]-m_all,2)

    for c in range(r):
        st+=pow(a3[c]-m_all,2)

    for d in range(r):
        st+=pow(a4[d]-m_all,2)

    #Sa計算
    sa=pow(m1-m_all,2)*r+pow(m2-m_all,2)*r+pow(m3-m_all,2)*r+pow(m4-m_all,2)*r

    #Se計算
    for e in range(r):
        se+=pow(a1[e]-m1,2)

    for f in range(r):
        se+=pow(a2[f]-m2,2)

    for g in range(r):
        se+=pow(a3[g]-m3,2)

    for h in range(r):
        se+=pow(a4[h]-m4,2)

    T=(sa/3)/(se/(4*r-4))

    if(T>x):
        print(j+1)
        print("棄却")
        count=count+1
    else:
        print(j+1)
        print("受容")

kensyutupower=count/100
print("１-β=")
print(kensyutupower)
