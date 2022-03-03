import pandas as pd
import numpy as np


seri1 = [0, 1, 2, np.nan, 2, 1, 0]
seri2 = [0, 1, 2, np.nan, np.nan, 2, 1.5, 0]


#Definition : Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
# d = {'a': 1, 'b': 2, 'c': 3}
# ser = pd.Series(data=d, index=['a', 'b', 'c'])

a  = pd.Series(seri1)
a1 = pd.Series(seri2)

#Definition : interpolate(method: str="linear", axis: Axis=0, limit: Optional[int]=None,
#                         inplace: bool_t=False, limit_direction: Optional[str]=None,
#                         limit_area: Optional[str]=None, downcast: Optional[str]=None, **kwargs)
#                     
#                          -> Optional[FrameOrSeries]

# s = pd.Series([0, 1, np.nan, 3])
# s
# 0    0.0
# 1    1.0
# 2    NaN
# 3    3.0
# dtype: float64

#  s.interpolate()
# 0    0.0
# 1    1.0 
# 2    2.0
# 3    3.0
# dtype: float64

#interpolation belli bir değerlerin derecesine göre ve yöntemine göre ortalamsını alıyor
#Tahmin. 

#örnek 1
b = a.interpolate()
b1= a1.interpolate()

#örnek 2
c = a.interpolate(method="polynomial", order = 2)
c1 = a1.interpolate(method="polynomial", order = 2)

#örnek 3
d = a.interpolate(method="polynomial", order = 1)
d1 = a1.interpolate(method="polynomial", order = 1)


print(b, end=' \n\n')
print(c, end=' \n\n')
print(d, end=' \n\n')

print(b1, end=' \n\n')
print(c1, end=' \n\n')
print(d1, end=' \n\n')

#########################################################
#datanın başlangıç de değişim konumlarını gösterir


#örnek 
print(a.iloc[0:],  end=' \n\n')
print(a.iloc[0:2], end=' \n\n')
print(a.iloc[1:2], end=' \n\n')
print(a.iloc[1:3], end=' \n\n')


