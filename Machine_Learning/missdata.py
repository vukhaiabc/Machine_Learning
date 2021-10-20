import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

my_df = pd.read_csv('mis_data.csv',header=None) #my_df dạng data frame
x = my_df.values   #chuyển đổi thành mảng
print(my_df)
imp = SimpleImputer(missing_values=np.nan,strategy = 'most_frequent')
imp.fit(x)
rs = imp.transform(x)
print("Sau khi chuyển đổi : ")
print(rs)