import pandas as pd

df = pd.read_csv('data/gemstone.csv')

df = df.drop(labels=['id'],axis=1)

# segregate numricals and categorical columns

numerical_columns = df.columns[df.dtypes!='object']
categorical_columns = df.columns[df.dtypes=='object']


import seaborn as sns
import matplotlib.pyplot as plt

# plt.figure(figsize=(8,6))
# x=0
# for i in numerical_columns:
#     sns.histplot(data=df,x=i,kde=True)
#     print("\n")
#     plt.show()


cut_map = {"Fair":1,"Good":2,"Very Good":3,"Premium":4,"Ideal":5}
df['clarity'].unique()

clarity_map = {"I1":1,"SI2":2 ,"SI1":3 ,"VS2":4 , "VS1":5 , "VVS2":6 , "VVS1":7 ,"IF":8}

color_map = {"D":1 ,"E":2 ,"F":3 , "G":4 ,"H":5 , "I":6, "J":7}

df['cut']=df['cut'].map(cut_map)
df['clarity'] = df['clarity'].map(clarity_map)
df['color'] = df['color'].map(color_map)

print(df.head())