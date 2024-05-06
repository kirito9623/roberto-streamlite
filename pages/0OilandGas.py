import streamlit as st
#!/usr/bin/env python
# coding: utf-8

# # U.S. Oil and Gas Production Analysis
# Analyzing the [Kaggle Dataset](https://www.kaggle.com/djzurawski/us-oil-and-gas-production-june-2008-to-june-2018) with information about Oil and Gas production in the US from June 2008 to June 2018.
# 

# In[4]:


import numpy as np
import pandas as pd
import matplotlib


# ---
# 
# Let's load the Gas production:

# In[11]:


file = "./data/U.S._crude_oil_production.csv"
gas_df = pd.read_csv(file, decimal=",")
gas_df.head(3)


# In[12]:


# Check how many rows and columns in the dataframe
gas_df.shape


# In[13]:


# Display all the available column names in the dataframe
gas_df.columns


# In[14]:


# Display additional info about each columns such as data types and number of non-null values
gas_df.info()


# In[41]:


gas_df['Month'] = pd.to_datetime(gas_df['Month'])
gas_df['Month']


# ### Check your code
# 

# In[43]:


print(gas_df['Month'].dtype)


# In[46]:


from nbresult import ChallengeResult
result = ChallengeResult('date',
    month_type=month_type,
)
result.write()


# In[47]:


print(result.check())


# In[28]:


gas_df['Month'].dt.year.head()


# In[48]:


gas_df['Month'].dt.month.tail()


# ---
# 
# ## Yearly Gas production

# In[70]:


# Agrupar por año y sumar la producción de gas para cada estado

yearly_gas_df = gas_df.groupby(gas_df['Month'].dt.year).sum()

# Agrupar solo por año y sumar la producción de gas para obtener el total anual de EE.UU.
filtered_yearly_gas_df = gas_df.groupby(gas_df['Month'].dt.year).sum().reset_index()
print("Producción Anual Desglosada por Estado:")
print(yearly_gas_df)

print("\nProducción Total Anual de EE.UU.:")
print(filtered_yearly_gas_df)


# ### Check your code
# 

# In[71]:


index_year = yearly_gas_df.index[0]
yearly_gas_shape = yearly_gas_df.shape
us_total = yearly_gas_df.iloc[0,0]


# In[72]:


from nbresult import ChallengeResult
result = ChallengeResult('full_gas',
    index_year=index_year,
    yearly_gas_shape=yearly_gas_shape,
    us_total=us_total
)
result.write()
print(result.check())


# ## State production
# 
# Let's have a look at the yearly production of some specific states

# In[73]:


filtered_yearly_gas_df.columns[1:].sort_values()


# In[74]:


plot = filtered_yearly_gas_df.filter(items=['Colorado', 'Louisiana', 'Ohio', 'Utah']).plot()
plot.set_xlabel("Year");


# ---
# 
# ## Comparing with Crude Oil Production

# In[80]:


oil_df = pd.read_csv('data/U.S._crude_oil_production.csv')


# In[81]:


# Analizar la columna 'Month' en un objeto de fecha y hora
oil_df['Month'] = pd.to_datetime(oil_df['Month'])


# ---
# 
# ## Yearly Oil production

# In[82]:


# Agrupar por año y sumar la producción de petróleo crudo para obtener el total anual de EE.UU.
yearly_oil_df = oil_df.groupby(oil_df['Month'].dt.year).sum().reset_index()

# Muestra las primeras filas del DataFrame resultante
print(yearly_oil_df.head())


# In[85]:


yearly_oil_df.columns = yearly_oil_df.columns.str.strip()


# In[86]:


yearly_oil_df.filter(items=['U.S. Crude Oil']).plot(kind='bar');


# In[90]:


# Asegurarse de que la columna 'Month' sea de tipo datetime
yearly_oil_df['Month'] = pd.to_datetime(yearly_oil_df['Month'])

# Filtrar para recopilar solo años con 12 meses completos
filtered_yearly_oil_df = yearly_oil_df[yearly_oil_df['Month'].dt.month == 12]

# Muestra las primeras filas del DataFrame resultante
print(filtered_yearly_oil_df.head())


# ### Check your code
# 

# In[91]:


from nbresult import ChallengeResult
result = ChallengeResult('oil',
    filtered_oil_shape=filtered_yearly_oil_df.shape,
    filtered_oil_index_year=filtered_yearly_oil_df.index[0],
    us_total=filtered_yearly_oil_df.iloc[0,0]
)
result.write()
print(result.check())


# In[93]:


plot = merged_df.plot(kind="bar")
plot.set_xlabel("Year")
plot.legend(['Gas (Millions of Cubic feet)', 'Crude Oil (Thousands of barrels)']);


# In[ ]:




