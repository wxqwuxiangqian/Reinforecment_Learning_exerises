import numpy as np
import pandas as pd
list=['x','y','z']
state=['1','2','3','4','5','6',]
np.random.seed(1)
table = pd.DataFrame(np.random.rand(6, len(list)),index=state,columns=list)
print (table)
#print(table.iloc[2, : ])
#print(0.1*table.iloc[2, : ].max())  # 取第二行所有
#print(table.iloc[ : ,2])  # 取第二lie所有
#print (table.iloc['x'])
print(np.random.choice(state))