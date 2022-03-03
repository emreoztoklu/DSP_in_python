import pandas as pd
import numpy as np

Data1= [1,2,3,4,5]
Data2= [10,20,30,40,50]
Data3= [5,7,9,12,15]

Data=  [Data1, Data2 ,Data3]

Columns = ['first', 'second', 'third', 'fourth', 'fifth']
Indeks  = ['row1', 'row2', 'row3']

df= pd.DataFrame(Data, columns = Columns, index = Indeks)



print(df, end='\n\n') 
#############################################
#      first  second  third  fourth  fifth
#row1      1       2      3       4      5
#row2     10      20     30      40     50
#row3      5       7      9      12     15
#############################################

print(df.query('first > 5'), end='\n\n')

#############################################
#      first  second  third  fourth  fifth
#row2     10      20     30      40     50
#############################################

print(df.query('first > 3 & second <10'), end='\n\n')

 #############################################
#      first  second  third  fourth  fifth
#row3      5       7      9      12     15
#############################################

print(df.query('first > 3 & second < 25'), end='\n\n')

#############################################
#       first  second  third  fourth  fifth
#row2     10      20     30      40     50
#row3      5       7      9      12     15
#############################################

print(df.query('first > 3 & second < 25').iloc[0], end='\n\n')
#yada
#print(df.query('first > 3 & second < 25').loc["row2"], end='\n\n')

#############################################
#first     10
#second    20
#third     30
#fourth    40
#fifth     50
#Name: row2, dtype: int64
#############################################

print(df.query('first > 3 & second < 25').iloc[1], end='\n\n')

#yada
#print(df.query('first > 3 & second < 25').loc["row3"], end='\n\n')

#############################################
#first     5
#second    7
#third     9
#fourth    12
#fifth     15
#Name: row3, dtype: int64
#############################################

print(df.query('second==20'), end='\n\n')

#############################################
#      first  second  third  fourth  fifth
#row2     10      20     30      40     50
#############################################
print(df['first'].iloc[2], end='\n\n')
print(df['first'].loc['row3'], end='\n\n')

np.random.randint
