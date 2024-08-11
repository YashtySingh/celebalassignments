#!/usr/bin/env python
# coding: utf-8

# In[56]:


import pandas as pd


# In[57]:


data = pd.read_csv('tour_package.csv')


# In[58]:


data.sample(10)


# In[59]:


data['Occupation'].value_counts()


# In[60]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[61]:


sns.countplot(x = 'Occupation', data = data)


# In[62]:


data['Gender'].value_counts()


# In[63]:


sns.countplot(x = 'Designation', data = data)


# In[64]:


#Exploratory data analysis


# In[65]:


# data.info()
# data.describe()
# data.sample(5)


# In[66]:


# find out categorial and continuos numerical data


# In[67]:


data.columns


# In[68]:


for col in data.columns:
    print(col,':', data[col].nunique())
    print('-'*10)
    print(data[col].value_counts())
    print( '--*--' * 10)


# In[69]:


data.columns


# In[70]:


cat_cols = ['CustomerID','CityTier','Occupation', 'Gender','ProductPitched', 'PreferredPropertyStar', 'MaritalStatus', 'Passport', 'PitchSatisfactionScore',
       'OwnCar',  'Designation','PitchSatisfactionScore']
num_cols = ['Age', 'DurationOfPitch','NumberOfPersonVisiting','PitchSatisfactionScore', 'NumberOfChildrenVisiting', 'MonthlyIncome']
drop_cols = ['CustomerID']
feat_cols =[]
target_col = 'ProdTaken'


# In[71]:


#missing data?
#outliners?
#dependent?


# In[72]:


pd.isnull(data).sum()


# In[73]:


100 * pd.isnull(data).sum() / len(data)


# In[74]:


#heatmap
plt.figure(figsize=(10,3))
_ = sns.heatmap(
    pd.isnull(data), cmap ='viridis', yticklabels=[]
)


# In[75]:


# drp the missing data
df = data.dropna()


# In[76]:


df.shape


# In[77]:


100 * pd.isnull(data).sum() / len(data)


# In[78]:


# Preprocessing the improper data


# In[79]:


df['Gender'].value_counts()


# In[80]:


#for i in df['Gender']:
  #  print(i)
  #  df['Gender'][pos?]
import warnings
warnings.filterwarnings('ignore')


# In[81]:


def GenderKoTheekKarneWala(gender):

    if gender == 'Fe Male':
        gender == 'Female'
        return gender


# In[82]:


df['Gender'] = df['Gender'].apply(GenderKoTheekKarneWala)


# In[83]:


df['Gender']= df['Gender'].str.replace('Fe Male','Female')


# In[84]:


# Univariate Analysis


# In[85]:


for col in cat_cols:
    sns.countplot(x=col,data = df)
    plt.show()


# In[86]:


sns.set_style('darkgrid')


# In[87]:


#Displot
for col in num_cols:
    sns.displot(x=col,data = df)
    plt.show()


# In[88]:


#Kdeplot
for col in num_cols:
    sns.kdeplot(x=col,data = df)
    plt.show()


# In[89]:


#barplot
for col in num_cols:
    sns.barplot(x=target_col, y=col, data = df)
    plt.show()


# In[ ]:


#countplot
for col in cat_cols:
    sns.countplot(x=col, hue = target_col,data = df)
    plt.show()


# In[91]:


for col in cat_cols:
    sns.countplot(x = col, hue = target_col, data = df)
    plt.show()


# In[92]:


sum((df['MaritalStatus'] == 'Single')
& (df['ProductPitched'] == 'Basic')
& (df['Designation'] == 'Executive'))


# In[93]:


sbe = df[((df['MaritalStatus'] == 'Single')
    & (df['ProductPitched'] == 'Basic')
    & (df['Designation'] == 'Executive'))]


# In[94]:


sbe['ProdTaken'].value_counts()


# ##### 

# In[95]:


191/225


# In[96]:


df['ProdTaken'].value_counts()


# In[97]:


797


# In[ ]:


#heat map
_=sns.heatmap(df[num_cols].corr(), annot = True)


# In[99]:


#multi-variate Analysis


# In[ ]:


#Scatterplot
for col1 in num_cols:
    for col2 in num_cols:
        if col1 != col2:
            sns.scatterplot(x = col, hue = target_col, data = df)
    plt.show()


# In[101]:


cat_cols


# In[102]:


for col1 in cat_cols:
    for col2 in num_cols:
        sns.boxplot(x = col1 ,y = col2, hue = target_col, data = df)
        plt.show()


# In[103]:


df.shape


# In[104]:


sns.boxplot(x = col1 ,y = col2, hue = target_col, data = df)


# In[105]:


num_cols


# In[106]:


sns.boxplot(x = col1 ,y = col2, hue = target_col, data = df)

