import pandas as pd
import numpy as np

data = [[1,2],[5,4],[7,8]]
columns_name = ['col1', 'col2']
rows_name = ['row1', 'row2','row3']


#Definition : DataFrame(data=None, index: Optional[Axes]=None, columns: Optional[Axes]=None,
#                        dtype: Optional[Dtype]=None, copy: bool=False)



#dizi array durumuna getirmekiçin kullanılan yapı matris


df = pd.DataFrame(data= data, index =rows_name, columns= columns_name)

df.index.name = 'satır'
df.columns.name = "Sütun"

print(df, end=" \n\n")

#
#       col1  col2
# row1     1     2
# row2     5     4
# row3     7     8 


print(df.iloc[0,1], end='\n\n')

# 2    => [0,1]



# iloc ilk değeri 0 ile 1 arasında 0:1 
# ikinci değerler ise 1 den sonra  1:
    
print(df.iloc[0:1, 1:], end='\n\n')     
                            # aralık verildi  0:1 arası 1, 1: sonrası 2
                            # o zmn 1,2 oda 2 değerine gelecek

#      col2
#row1     2


print(df.iloc[0:, 0:], end='\n\n')

#      col1  col2
#row1     1     2
#row2     5     4
#row3     7     8

################################################
# veri = [0, 1, 2, np.nan, np.nan, 2, 1.5, 0]
#
# for i  in range (0, len(veri)):
#    print(i)
################################################

