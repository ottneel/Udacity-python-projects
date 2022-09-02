#!/usr/bin/env python
# coding: utf-8

# ## Reporting: wragle_report
# * Create a **300-600 word written report** called "wrangle_report.pdf" or "wrangle_report.html" that briefly describes your wrangling efforts. This is to be framed as an internal document.

# # Gathering Efforts

# i firstly imported the pandas library as pd, then read the 'twitter_enhanced_csv' file into the we rate dogs variable.
# then I used the requests library to download the image prediction_tsv file.
# next, i made use of the Twitter API to extract the tweet_json.txt data and saved it to a file tweet_json.txt.

# # Accessing Efforts

# i made use of both the visual assessment and the programmatic assessment to assess the three dataframes and come up with the following Quality and tidiness issues
# 1. Alot of the columns had missing data which I dropped some as they weren't going to be needed
# 2. we_rate_dogs_df Timestamp column was am object or string and needed to be changed to a datetime type
# 3. tweet_id in we_rate_dogs_df was to be changed from int to a str
# 4. id in tweet_json was also to be changed from int to str
# 5. tweet_id in image prediction was to be changed from int to str
# 6. columns in tweet_json with missing data were dropped
# 7. renaming of id in json_tweet to tweet_id
# 8. dropping irrelevant columns in json_tweet

# ### tidiness issues

# 1. p1 p2 p3 were to be rerranged to a single and relevant columns
# 2. the numerator and denominator columns was to be combined to a single column called rating

# # Cleaning Efforts

# The above mentioned issues were properly cleaned using the necessary techniques available in pandas and python while the 3 dataframes were combined and appended into a single Master dataframe

# # Storing Data

# The Master dataframe was now stored as a CSV file called the 'twitter_archive_master.csv' file

# # Analyzing and Visualization Efforts

# Insights and visualizations that were made, was reported in the act report file

# In[ ]:




