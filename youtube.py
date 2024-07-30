#!/usr/bin/env python
# coding: utf-8
#data analyst at Intern Career Task 1
# In[2]:


import pandas as pd
data=pd.read_csv("youtubers_df.csv")
data.head()


# In[3]:


data.rename(columns={'Suscribers': 'Subscribers'}, inplace=True)


# In[3]:


data.head()


# In[5]:


data.info()


# In[7]:


data['Subscribers'] = data['Subscribers'].astype(int)
data['Visits'] = data['Visits'].astype(int)
data['Likes'] = data['Likes'].astype(int)
data['Comments'] = data['Comments'].astype(int)
data.info()


# In[15]:


data=data.dropna(axis=0)  
data.shape


# In[16]:


data.describe()


# In[17]:


correlation_matrix = data[['Subscribers', 'Likes', 'Comments']].corr()
correlation_matrix


# The value is 0.248389. This indicates a positive but weak correlation. This means that as the number of subscribers increases, the number of likes tends to increase, but the relationship is not very strong.
# The value is 0.037293. This indicates a very weak positive correlation. This suggests that there is almost no relationship between the number of subscribers and the number of comments.
# 

# In[18]:


import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix Heatmap')
plt.show()


# In[26]:


country_counts = data['Country'].value_counts()
plt.figure(figsize=(12, 6))
sns.barplot(x=country_counts.index, y=country_counts.values)
plt.title('Distribution of Streamers by Country')
plt.xlabel('Country')
plt.ylabel('Number of Streamers')
plt.xticks(rotation=90)
plt.show()


# In[37]:


average_metrics = data[['Subscribers', 'Visits', 'Likes', 'Comments']].mean()
average_metrics


# The average number of subscribers is extremely high (22 million). This suggests that the dataset consists of very popular YouTube streamers
# The average number of visits (1.2 million) is significantly lower than the number of subscribers.This could imply that while these streamers have a large subscriber base, only a portion of the subscribers regularly visit the streamer's content.
# The average number of likes (53,473) is much lower than the number of visits.This pattern is expected since not all viewers who visit the content will like it. 
# The average number of comments (1,559) is the lowest among the metrics.
# This suggests that a very small percentage of viewers engage with the content by commenting. This is typical as commenting requires more effort compared to liking a video.
# 

# In[39]:


# Define the average metrics
average_metrics = pd.Series({
    'Subscribers': 2.241556e+07,
    'Visits': 1.210730e+06,
    'Likes': 5.347360e+04,
    'Comments': 1.558794e+03
})

plt.figure(figsize=(10, 6))
sns.barplot(x=average_metrics.index, y=average_metrics.values, palette='viridis')
plt.yscale('log')  # Using log scale for better visualization of large differences
plt.title('Average Number of Subscribers, Visits, Likes, and Comments')
plt.xlabel('Metric')
plt.ylabel('Average Count (Log Scale)')
plt.show()


# There is a clear pattern of decreasing engagement from subscribers to visits to likes to comments. This is expected as the level of engagement effort increases.
# 

# In[52]:


counts = data['Categories'].value_counts()
plt.figure(figsize=(12, 6))
sns.lineplot(x=counts.index, y=counts.values, marker='o')
plt.title('Distribution of Streamers by Country')
plt.xlabel('CATEGORIES')
plt.ylabel('Number of Streamers')
plt.xticks(rotation=90)
plt.show()


# In[54]:


above_average_streamers = data[
    (data['Subscribers'] > average_metrics['Subscribers']) &
    (data['Visits'] > average_metrics['Visits']) &
    (data['Likes'] > average_metrics['Likes']) &
    (data['Comments'] > average_metrics['Comments'])
]
top_performers = above_average_streamers.sort_values(by='Subscribers', ascending=False)
top_performers


# MrBeast is the top  on the basis of Subscribers as compare to other content creaters






