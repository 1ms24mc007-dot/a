import pandas as pd
df=pd.DataFrame({'col1':[1,2,3,4],'col2':['A','B','C','D'],'col3':[111,222,333,444]})
df
df.head()
df.tail()
df.count()
df['col2'].count()

df1.dropna()
del df['col1']
df1.sort_values('col2')
df.fillna('FILLED')
