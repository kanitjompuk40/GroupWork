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
    df
        Sales data in a melted format
    """
    
    df_melt = df.sample(n=items).copy().reset_index(drop=True)
    df_melt = df_melt.iloc[:, :days+6]
    
    df_melt = pd.melt(df_melt, id_vars=['id', 'item_id', 'dept_id', 'cat_id', 'store_id', 'state_id'], 
                 var_name='d', value_name='sold')
    
    return df_melt
