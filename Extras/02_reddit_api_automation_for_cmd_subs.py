#!/usr/bin/env python
# coding: utf-8

# In[1]:


# citing : Sara Soueidan - Project 3, Tim Book - API Code; Zoom recording DSIR-824


# In[3]:


# imports
import pandas as pd
import numpy as np

# APi
import requests

# automating - use for time based operations
import time
import datetime
import sys
from time import sleep


# In[4]:


# build a api function,  to automate the process
# define function, with subreddit, # of times function should run
def get_posts(subreddit, n_iter, epoch_right_now):
    # store base url
    base_url = 'https://api.pushshift.io/reddit/search/submission/?subreddit='
    # create empty list
    df_list = []
    # set epoch to current time
    current_time = epoch_right_now
    #set up for loop
    for post in range(n_iter):
        # get requests
        res = requests.get(
            # base url for response variable
            base_url,
            # parameters for response
            params = {
                # subreddit
                'subreddit' : subreddit,
                # size
                'size'      : 80,
                # lang == True
                'lang'      : True,
                # before this time pull everything
                'before'    : current_time} # close parameters
        ) # close .get
        # take data from most recent request, store as df
        df = pd.DataFrame(res.json()['data'])
        # pull specific columns for df
        df = df[['subreddit', 'selftext', 'title', 'created_utc', 'author', 'permalink']]
        # create submission_title column
#         link_list = list(df['permalink'].str.split('/'))
#         sub_list = []
#         for i in link_list:
#             sub_list.append(i[5])
#         df['submission_title'] = sub_list
#         #drop permalink column
#         df.drop(columns='permalink', inplace=True)
        # append to empty dataframe list
        df_list.append(df)
        # set current time counter back to last epoch in recently appended df
        current_time = df['created_utc'].min()
        #set sleep time
        time.sleep(10)
    #return one df for all requests
    return pd.concat(df_list, axis=0)


# In[5]:


# create large df of both subreddits
reddit_df = pd.concat([get_posts('sportsbook', 10, 1616965200), get_posts('dfsports', 10, 1616965200)])


# In[19]:


# output to csv
reddit_df.to_csv('Comments/reddit_subs.csv')
