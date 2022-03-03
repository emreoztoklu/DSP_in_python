# -*- coding: utf-8 -*-
"""
DENEME GEÇEN ÖDEV
"""

import numpy as np
import pandas as pd 


data = np.random.randint(0,10,size=(4,5))

Col_names =["var1","var2","var3","var4","var5"]
df = pd.DataFrame(data, columns=Col_names)
print(df)


def Process(column_name, column_name2, en_buyul_var):    
    if column_name == "var5":
        column_name2 = "var1"
    else:
        column_name2 = column_name2
        
    #print(column_name)
    #print(column_name2)
    #print(str(en_buyul_var))
    
    index_var = df.index
    condition = df[column_name] == en_buyul_var
    index_var = index_var[condition].tolist()
    index_var2= index_var[0]
    index_var.clear()
    
    #print(index_var2)
    
    a = df.loc[index_var2, column_name2]
    b = df.loc[index_var2, column_name2]
    df[column_name2] = df[column_name2.replace(a, b)
    
    #return(df)

 en_buyuk_var1 = df.loc[0,"var1"]    
 en_buyuk_var2 = df.loc[0,"var2"]        
 en_buyuk_var3 = df.loc[0,"var3"]    
 en_buyuk_var4 = df.loc[0,"var4"]    
 en_buyuk_var5 = df.loc[0,"var5"]



for i in range(1,4):
    if df.loc[i, "var1"] > en_buyuk_var1:
        en_buyuk_var1 = df.loc[i, "var1"]
        
     if df.loc[i, "var2"] > en_buyuk_var1:
        en_buyuk_var2 = df.loc[i, "var2"]

    if df.loc[i, "var3"] > en_buyuk_var1:
        en_buyuk_var3 = df.loc[i, "var3"]

    if df.loc[i, "var4"] > en_buyuk_var1:
        en_buyuk_var4 = df.loc[i, "var4"] 

    if df.loc[i, "var5"] > en_buyuk_var1:
        en_buyuk_var5 = df.loc[i, "var5"]

