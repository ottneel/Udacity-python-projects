#!/usr/bin/env python
# coding: utf-8

# # Project: Wrangling and Analyze Data

# ## Data Gathering
# In the cell below, gather **all** three pieces of data for this project and load them in the notebook. **Note:** the methods required to gather each data are different.
# 1. Directly download the WeRateDogs Twitter archive data (twitter_archive_enhanced.csv)

# In[1]:


#import the pandas library first
import pandas as pd
we_rate_dogs_df= pd.read_csv('twitter-archive-enhanced.csv')


# In[2]:


we_rate_dogs_df.head()


# In[3]:


tweet_id_list=we_rate_dogs_df['tweet_id'].tolist()


# In[4]:


#tweet_id_list


# 2. Use the Requests library to download the tweet image prediction (image_predictions.tsv)

# In[5]:


import requests
url='https://d17h27t6h515a5.cloudfront.net/topher/2017/August/599fd2ad_image-predictions/image-predictions.tsv'
response= requests.get(url)
file_name= 'image_prediction.tsv'
with open (file_name, mode = 'wb') as file:
    file.write(response.content)
image_predictions_df = pd.read_csv('image_prediction.tsv', sep='\t')


# 3. Use the Tweepy library to query additional data via the Twitter API (tweet_json.txt)

# In[6]:


import tweepy
import json
from timeit import default_timer as timer

consumer_key= ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api=tweepy.API(auth, wait_on_rate_limit=True)


# count = 0
# fails_dict = {}
# start = timer()
# # Save each tweet's returned JSON as a new line in a .txt file
# with open('tweet_json.txt', 'w') as outfile:
#     # This loop will likely take 20-30 minutes to run because of Twitter's rate limit
#     for tweet_id in tweet_id_list:
#         count += 1
#         print(str(count) + ": " + str(tweet_id))
#         try:
#             tweet = api.get_status(tweet_id, tweet_mode='extended')
#             print("Success")
#             json.dump(tweet._json, outfile)
#             outfile.write('\n')
#         except tweepy.TweepError as e:
#             print("Fail")
#             fails_dict[tweet_id] = e
#             pass
# end = timer()
# print(end - start)
# print(fails_dict)

# In[7]:


json_tweet_df = pd.read_json('tweet_json.txt', lines=True)


# ## Assessing Data
# In this section, detect and document at least **eight (8) quality issues and two (2) tidiness issue**. You must use **both** visual assessment
# programmatic assessement to assess the data.
# 
# **Note:** pay attention to the following key points when you access the data.
# 
# * You only want original ratings (no retweets) that have images. Though there are 5000+ tweets in the dataset, not all are dog ratings and some are retweets.
# * Assessing and cleaning the entire dataset completely would require a lot of time, and is not necessary to practice and demonstrate your skills in data wrangling. Therefore, the requirements of this project are only to assess and clean at least 8 quality issues and at least 2 tidiness issues in this dataset.
# * The fact that the rating numerators are greater than the denominators does not need to be cleaned. This [unique rating system](http://knowyourmeme.com/memes/theyre-good-dogs-brent) is a big part of the popularity of WeRateDogs.
# * You do not need to gather the tweets beyond August 1st, 2017. You can, but note that you won't be able to gather the image predictions for these tweets since you don't have access to the algorithm used.
# 
# 

# For the visual assessment, i will use the sample function to take a sample of each dataframe. my findings will be documented in the list of Quality issues below

# In[8]:


we_rate_dogs_df.sample(10)


# In[9]:


image_predictions_df.sample(5)


# In[10]:


json_tweet_df.sample(10)


# For the programatic assessment, i will be making use of the info, duplicate, nunique and dtype functions.

# In[11]:


we_rate_dogs_df.info()


# In[12]:


image_predictions_df.info()


# In[13]:


json_tweet_df.info()


# In[14]:


we_rate_dogs_df.duplicated().sum()


# In[15]:


we_rate_dogs_df.nunique().sum()


# In[16]:


we_rate_dogs_df.dtypes


# In[17]:


image_predictions_df.duplicated().sum()


# In[18]:


image_predictions_df.nunique().count()


# In[19]:


image_predictions_df.dtypes


# In[20]:


json_tweet_df.info()


# # Quality issues
# 1.we_rate_dogs_df and json_tweet_df, have rows with missing data
# 
# 2.tweet_id and Timestamp should be objects and datetime in we_rate_dogs_df respectively
# 
# 3.tweet_id in image_predictions should be an object datatype
# 
# 4.in json_tweet_df, id Should be an object datatype
# 
# 5.id in json_tweet_df should be renamed as tweet_id to be consistent with other ids from image predictions and we_rate_dogs_df.
# 
# 6.In the image prediction df, the column labels p1,p2,p3 will have to be renamed.
# 
# 7.The name column has many wrong names like , a, an, the.

# 8.removal of Retweets and replies.

# # Tidiness issues
# 1.In the we_rate_dogs_df, the Dog type, should be under a single column
# 
# 2.The three dataframes should be appended as one

# ## Cleaning Data
# In this section, clean **all** of the issues you documented while assessing. 
# 
# **Note:** Make a copy of the original data before cleaning. Cleaning includes merging individual pieces of data according to the rules of [tidy data](https://cran.r-project.org/web/packages/tidyr/vignettes/tidy-data.html). The result should be a high-quality and tidy master pandas DataFrame (or DataFrames, if appropriate).

# In[21]:


# Make copies of original pieces of data
dog_rates_copy=we_rate_dogs_df.copy()
image_copy=image_predictions_df.copy()
json_tweet_copy=json_tweet_df.copy()


# ### Issue #1:

# # Define:
# there's not a lot that I can do with missing Data. buti could delete some of the columns with Missing data

# #### Code

# In[22]:


dog_rates= dog_rates_copy.drop(['in_reply_to_status_id','in_reply_to_user_id','retweeted_status_user_id','expanded_urls','retweeted_status_timestamp'],axis=1, inplace=True)


# #### Test

# In[23]:


dog_rates_copy


# ### Issue #2:

# # Define 
# change we_rate_dogs timestamp column from object to datetime

# #### Code

# In[24]:


dog_rates_copy['timestamp']=pd.to_datetime(dog_rates_copy['timestamp'])


# In[25]:


dog_rates_copy['tweet_id']=dog_rates_copy.tweet_id.astype(str)


# ### test

# In[26]:


dog_rates_copy.timestamp.dtypes


# In[27]:


dog_rates_copy.dtypes


# ## issue 3

# # Define
# 
# The name column in we_rate_dogs_df has many invalid values like , a, an, the.

# ### code

# In[28]:


incorrect_names = list(dog_rates_copy.query('name == "a" or name == "an" or name== "the" or name== "quite" or name=="such" ').index)
for i in incorrect_names:     
    dog_rates_copy.name[i]= "None"


# ### test

# In[29]:


dog_rates_copy['name'].sample(10)


# ## issue 4

# # Define
# tweet_id in image prediction will be changed to an object

# ### code

# In[30]:


image_copy.tweet_id=image_copy.tweet_id.astype(str)


# ### test

# In[31]:


image_copy.tweet_id.dtypes


# ## issue 5

# # Define
# change the datatype of id in json_tweet from int to obj datatype

# ### code

# In[32]:


json_tweet_copy.id= json_tweet_copy.id.astype(str)


# ### test

# In[33]:


json_tweet_copy.id.dtypes


# ## issue 6

# # Define
# 
# i will now remove Retweets and replies rows

# ### code

# In[34]:


retweets_index = list(dog_rates_copy[dog_rates_copy["retweeted_status_id"].isnull()==False].index)


# In[35]:


dog_rates_copy.drop(axis=0, index=retweets_index, inplace=True)


# ## test

# In[36]:


for retweet in retweets_index:
    if retweet in list(dog_rates_copy.index):
        print('Found a retweet')
    else:
        print('no retweets found')


# ## issue 7

# # Define
# Use the rename function to change the id in json_tweet to tweet_id

# ### code

# In[37]:


json_tweet_copy=json_tweet_copy.rename(columns={'id':'tweet_id'})


# ### test

# In[38]:


tweet_id_coln=json_tweet_copy["tweet_id"]
tweet_id_coln.sample(5)


# ## issue 8

# # Define
# 
# Drop unneeded columns in json_tweet

# ## code

# In[39]:


json_tweet_copy.drop(['id_str','is_quote_status','lang','truncated','source'], axis=1, inplace =True)


# In[40]:


json_tweet_copy.drop(['entities','display_text_range'], axis =1, inplace= True)


# ### test

# In[41]:


json_tweet_copy.info()


# # TIDINESS ISSUES

# ## Issue 1

# # Define
# p1, p2, p3 and p1,p2 ,p3 confidence and p1,p2,p3 dogs will be put under different columns headers

# In[42]:


prd1 = image_copy.drop(columns=['p3','p3_conf','p3_dog','p2','p2_conf','p2_dog'])
prd1['prediction_no'] = 'one'
prd2 = image_copy.drop(columns=['p1','p1_conf','p1_dog','p3','p3_conf','p3_dog'])
prd2['prediction_no'] = 'two'
prd3 = image_copy.drop(columns=['p1','p1_conf','p1_dog','p2','p2_conf','p2_dog'])
prd3['prediction_no'] = 'three'
prd1 = prd1.rename(columns = {"p1": "predictions", "p1_conf":"confidence_levels", "p1_dog": "dog_type"}) 
prd2 = prd2.rename(columns = {"p2": "predictions", "p2_conf":"confidence_levels", "p2_dog": "dog_type"}) 
prd3 = prd3.rename(columns = {"p3": "predictions", "p3_conf":"confidence_levels", "p3_dog": "dog_type"}) 
image_copy = prd1.append(prd2, ignore_index = True).append(prd3, ignore_index = True) 


# In[43]:


image_copy.sample(5)


# ## issue 2

# # Define
# combine the numerator and denominator columns into one song column called rating

# ### code

# In[44]:


dog_rates_copy[['rating_numerator','rating_denominator']]=dog_rates_copy[['rating_numerator','rating_denominator']].astype(str)


# In[45]:


dog_rates_copy['rating']=dog_rates_copy[['rating_numerator','rating_denominator']].apply('/'.join, axis=1)


# In[46]:


dog_rates_copy.rating.sample(5)


# In[47]:


dog_rates_copy.drop(['rating_numerator','rating_denominator'],axis=1,inplace=True)


# ### test

# In[48]:


dog_rates_copy.sample(5)


# ### issue 3

# # Define
# 
# In the we_rate_dogs_df, the Dog type, should be under a single column

# ### code

# In[49]:


dog_rates_copy['type']=None
dog_rates_copy['type'] = dog_rates_copy.doggo + dog_rates_copy.floofer + dog_rates_copy.pupper + dog_rates_copy.puppo


# In[50]:


dog_rates_copy['type'] = dog_rates_copy['type'].map(lambda x: x.replace("None",""))
dog_rates_copy.loc[dog_rates_copy.type == 'doggopupper', 'type'] = 'doggo, pupper'
dog_rates_copy.loc[dog_rates_copy.type == 'doggopuppo', 'type'] = 'doggo, puppo'
dog_rates_copy.loc[dog_rates_copy.type == 'doggofloofer', 'type'] = 'doggo, floofer'


# In[51]:


dog_rates_copy.drop(['doggo','floofer','pupper','puppo'], axis=1, inplace=True)


# ### test

# In[52]:


dog_rates_copy.sample(10)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[53]:


master_df = pd.merge(dog_rates_copy,image_copy, on ='tweet_id')


# In[54]:


master_df = pd.merge(master_df,json_tweet_copy, on ='tweet_id')


# In[55]:


master_df.info()


# In[56]:


master_df.sample(5)


# ## Storing Data
# Save gathered, assessed, and cleaned master dataset to a CSV file named "twitter_archive_master.csv".

# In[57]:


master_df.to_csv('twitter_archive_master.csv',index = False)


# ## Analyzing and Visualizing Data
# In this section, analyze and visualize your wrangled data. You must produce at least **three (3) insights and one (1) visualization.**

# ### Questions:
# 1.which dogtype had the highest number of likes and retweets?
# 
# 2.what is the correlation between the likes and retweet
# 
# 3.which dogtype has the lowest number of likes and retweet

# In[65]:


popular_dogs= master_df.nlargest(3,['favorite_count','retweet_count'])


# In[71]:


popular_dogs[['type', 'favorite_count','retweet_count']]


# In[68]:


least_favorite= master_df.nsmallest(3,['favorite_count','retweet_count'])


# In[72]:


least_favorite[['type','favorite_count','retweet_count']]


# ## insights

# 1. i can see that the "doggo" dogtype was the most liked dog.
# 2. the least liked dogtype unfortunately didn't have an type.
# 3. The correlation between the favorite_count and the retweet_count was positive

# ### Visualization

# In[62]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
master_df.plot(kind='scatter', x='favorite_count', y='retweet_count').set_title('Likes Count V.S. Retweet Count')
plt.savefig('like_vs_retweet.png')


# In[63]:


master_df.favorite_count.hist(figsize=(10,8))
title=('histogram of fav_count')
plt.savefig('hist_fav_count.png')


# In[64]:


master_df.retweet_count.hist(figsize=(10,8))
title=('histogram of rt_count')
plt.savefig('hist_rt_count.png')

