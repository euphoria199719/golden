import pandas as pd
df=pd.read_csv('titanic.csv')#to read the csv file
print("Dataset Info:")#analysing the dataset
print(df.info())
df.dropna(inplace=True)#Data cleaning by removing rows with empty cells 
df['Age'].fillna(df['Age'].mean(),inplace=True)#replacing the empty values
df['Fare'].fillna(0,inplace=True)#replacing for specific columnn
df.fillna(df.mean(),inplace=True)#replacing each col using mean,median,mode
df['Age']=df['Age'].astype(int)#checking & converting the dataset 
df.loc[df['Age']>100,'Age']=100#replacing using the boundary values 
df.drop_duplicates(inplace=True)#removing the duplicate values
correlations=df.corr()#finding correlations
print("Correaltion:")
print(correlations)
print("Dataset after cleansing")
print("Number of passengers survived: ",df[df["Survived"] ==1]["Survived"].count())
print("Highest Age:",df['Age'].max())
print("Lowest Age:",df['Age'].min())
print("Average Age:",round(df['Age'].mean()))
print("No of male passengers=",df[df["Sex"] =='male']["Sex"].count())
print("No of female passengers=",df[df["Sex"] =='female']["Sex"].count())
max_fare_index=df['Fare'].idxmax()
min_fare_index=df['Fare'].idxmin()
print("Passenger with max fare:")
print(df.loc[max_fare_index])
print("Passenger with min fare:")
print(df.loc[min_fare_index])
df['Passenger type']='child'
df.loc[df['Age']>=60,'Passenger type']='Senior citizen'
df.loc[(df['Age']>=18)&(df['Age']<60),'Passenger type']='Adult'
print("No of child passengers=",df[df["Passenger type"] =='child']["Passenger type"].count())
df=df[df['Parch']<5]
print("Dataset after parch")
print(df.info())
df.to_csv('titanic_modified.csv',index=False)
df=pd.read_csv('titanic_modified.csv')#to read the csv file
print("Modified Dataset Info:")#analysing the dataset
print(df.info())
