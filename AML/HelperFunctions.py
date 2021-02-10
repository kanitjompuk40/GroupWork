#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:28:06 2021

@author: mattwear
"""

###M5 Helper Functions

import pandas as pd

def meltM5(df, days = 1941, items = 30490):
    """Function returns melted version of M5 sales data

    Parameters
    ----------
    df : Pandas DataFrame
        M5 Sales data
    days : int
        How many days of sales to include (default is all 1941 days)
    items: int
        How many items to include (default is 30490)

    Returns
    -------
    df_melt
        Sales data in a melted format
    """
    
    #Random sample of items items
    df_melt = df.sample(n=items).copy().reset_index(drop=True)
    #Subset to include specified number of days
    df_melt = df_melt.iloc[:, :days+6]
    #Melt
    df_melt = pd.melt(df_melt, id_vars=['id', 'item_id', 'dept_id', 'cat_id', 'store_id', 'state_id'], 
                 var_name='d', value_name='sold')
    
    return df_melt

def joinDataSets(melt_df, calendar_df, prices_df):
    """Function joins melted dataframe with calendar and sell price dataframes

    Parameters
    ----------
    melt_df : Pandas DataFrame
        Melted form of original data set
    calendar_df : Pandas DataFrame
        Calendar dataframe
    prices_df : Pandas DataFrame
        sell prices dataframe

    Returns
    -------
    df_joined
        Combined all available data into one dataframe in melted format
    """
    #Join calendar data
    df_joined = pd.merge(melt_df, calendar_df, on='d', how='left')
    #Join sell prices data
    df_joined = pd.merge(df_joined, prices_df, on=['store_id','item_id','wm_yr_wk'], how='left') 

    return df_joined










