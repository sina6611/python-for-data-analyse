#command
#import numpy as np
#import pandas as pd
# pd.DataFrame(randn(n,m),[Xlable],[Ylable])
# df['A']
#df.drop['A',axis=0,inplace=True]
#df.shape
#df.loc['B'] row selection
# df.loc['A','C']
# df.iloc[[1,2],[2,4]]
#df.loc[['C','G'],['B','G']]
#df[(df['1']>0) & (df['2']<0)]
#df.reset_index()
#state='NR BD VG JH LK IJ ZG RT ZT FD'
#state_lis=state.split()
#df['States']=state_lis
# a=[1,121,13]  b=[14,4,5]  hier_index=list(zip(a,b))
#df.set_index('States')
#hier_index=pd.MultiIndex.from_tuples(hier_index)  multi level data frame
#d={'A':[1,2,np.nan],'B':[54,25,63],'C':[np.nan,25,89]}
#df=pd.DataFrame(d)
#df.dropna(thresh=1)
#df.fillna('Fill value')
#group=df.groupby('Company')
#group.mean()
#df.describe()
#df.describe().transpose()