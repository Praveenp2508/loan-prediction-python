# dataframe

import pandas as pd

import pandas as pd
a=pd.DataFrame([1,2,3,4,5])
print(a)

import pandas as pd
a=['praveen',22],['sandy',23],['ruthesh',22]
b=pd.DataFrame(a,index=[1,2,3],columns=['name','age'])
print(b)

import pandas as pd
dict1={'ID':[101,102,103,104],'Name':['praveen','vicky','abi','sandy'],'Age':[22,23,34,43]}
d=pd.DataFrame(dict1,index=[1,2,3,4])
print(d)


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv('data of set.csv')
print(df.shape)
print(df.dtypes)
print(df.rename(columns={'name':'Name'}))
print(df.info())
print(df['Gender'])
print(df.isnull)
print(df.isnull().sum())
print(df.loc[:,['Loan_ID','Gender']])
print(df.loc[:,['Married','Education','LoanAmount']])
print(df.head())
print(df.loc[5:9,['Loan_ID','Gender']])
print(df.iloc[-5:-2])
print(df.describe())
print(df.describe(include='all'))
# print(df.dropna('tamil',axis=1,inplace=True))
print(df['Gender'].unique())
print(df.to_csv('updated student marks'))


#concat format

import pandas as pd
import numpy as np
dict1={'ID':[101,102,103,104],'Name':['praveen','vicky','abi','sandy'],'Age':[22,23,34,43]}
dict2={'ID':[105,106,107,108],'Name':['ruth','naveen','balaji','venkat'],'Age':[40,33,64,55]}
d=pd.DataFrame(data=dict1)
d1=pd.DataFrame(data=dict2)
df1=pd.concat([d,d1],ignore_index=True)
print(df1)