#!/usr/bin/env python
# coding: utf-8

# ## Report: act_report
# * Create a **250-word-minimum written report** called "act_report.pdf" or "act_report.html" that communicates the insights and displays the visualization(s) produced from your wrangled data. This is to be framed as an external document, like a blog post or magazine article, for example.

# After i had made efforts to clean and assess, the following insights were made
# 1. which dogs had the highest no of likes and retweets (top 3)
# 2. what is the correlation between the likes and the retweet
# 3. which dogs had the lowest no of likes and retweets

# Using the 'nlargest' function for the largest 3 dogs, i found out that the dogs nicknamed 'doggo' were the ones that was most liked and retweeted the most by the tweeter community as they all had almost 150,000 likes and 70,000 retweets

# i also made a histogram of the favorite count of the master df and found out that the favorite count nwss skewed greatly to the right.

# ![hist_rt_count.png](attachment:hist_rt_count.png)

# on the least favorite, they all had 0 likes and a retweet count of 26-29 which is pretty low, this might have been as a result of the fact that they were all retweets and not the original tweets made

# Also on the correlation between the likes and the retweets count, it was found out that they was a very serious positive correlation between the two of them meaning the tweets with the most likes were also retweeted the most 

# ![like_vs_retweet.png](attachment:like_vs_retweet.png)

# Also i did a histogram of the retweet counts and also noticed a strong skewness to the right of the rt_count histogram

# ![hist_rt_count.png](attachment:hist_rt_count.png)

# In[ ]:




