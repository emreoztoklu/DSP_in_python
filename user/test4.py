import pandas as pd
import numpy as np


Size_Matris = (5,3)
Rand_data = np.random.randint(1,30,size=Size_Matris)
print(Rand_data, end='\n\n')

Columns =['random_num1','random_num2','random_num3']
indexs  =['1.', '2.', '3.', '4.', '5.']

df=pd.DataFrame(Rand_data, columns=Columns, index = indexs)
print(df, end='\n\n')

