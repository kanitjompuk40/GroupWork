#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:28:06 2021

@author: mattwear
"""

###M5 Helper Functions

import pandas as pd
import os
import random

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

def joinDataSets(melt_df, calendar_df, prices_df, dropPriceNA=True):
    """Function joins melted dataframe with calendar and sell price dataframes

    Parameters
    ----------
    melt_df : Pandas DataFrame
        Melted form of original data set
    calendar_df : Pandas DataFrame
        Calendar dataframe
    prices_df : Pandas DataFrame
        sell prices dataframe
    dropPriceNA: boolean, optional
        drop rows for which a sell price is not given (since this means that the 
        product was not on sale that day), default is True

    Returns
    -------
    df_joined
        Combined all available data into one dataframe in melted format
    """
    #Join calendar data
    df_joined = pd.merge(melt_df, calendar_df, on='d', how='left')
    #Join sell prices data
    df_joined = pd.merge(df_joined, prices_df, on=['store_id','item_id','wm_yr_wk'], how='left') 
    #Drop rows where sell price is na
    if dropPriceNA:
        df_joined.dropna(subset=['sell_price'], inplace=True)
        
    return df_joined




def load_calendar_data():    
    csv_path = os.path.join('data', 'calendar.csv')
    return pd.read_csv(csv_path)


def load_sell_price_data():
    csv_path = os.path.join('data', 'sell_prices.csv')
    return pd.read_csv(csv_path)


def load_sales_train_validation_data():
    csv_path = os.path.join('data', 'sales_train_validation.csv')
    return pd.read_csv(csv_path)


def load_sales_train_evaluation_data():
    csv_path = os.path.join('data', 'sales_train_evaluation.csv')
    return pd.read_csv(csv_path)


def load_meltedJoined_data():    
    csv_path = os.path.join('data', 'meltedJoinedDf.csv')
    return pd.read_csv(csv_path)

def load_reduced_data():    
    csv_path = os.path.join('data', 'reduced.csv')
    return pd.read_csv(csv_path)



def reduceDataset(df, cuttOffDate = "2011-06-29", numberOfProducts = 500):
    df_reduced = df.loc[df["date"] < cuttOffDate]
    random_products = random.choices(list(set(df_reduced["id"])), k = numberOfProducts)
    return(df_reduced[df_reduced['id'].isin(random_products)])
    
    
def cleanDates(df):
    #Drops weekday, date and wm_yr_wk and creates a weekend binary indicator
    df.drop(['weekday','date','wm_yr_wk'], axis=1, inplace=True)
    df = df.assign(weekend=lambda df: df.apply(lambda row: 1 if row.wday == 1 or row.wday == 2 else 0, axis=1))
    return df

def cleanEvents(df):
    #Drops type of events and creates binary indicators for the 4 types of event plus one for christmas
    df=df.assign(sporting=lambda df:df.apply(lambda row: 1 if row.event_type_1=="Sporting" 
                                                         or row.event_type_2=="Sporting" else 0,axis=1))
    df=df.assign(cultural=lambda df:df.apply(lambda row: 1 if row.event_type_1=="Cultural" 
                                                         or row.event_type_2=="Cultural" else 0,axis=1))
    df=df.assign(national=lambda df:df.apply(lambda row: 1 if row.event_type_1=="National" 
                                                             or row.event_type_2=="National" else 0,axis=1))
    df=df.assign(religious=lambda df:df.apply(lambda row: 1 if row.event_type_1=="Religious" 
                                                            or row.event_type_2=="Religious" else 0,axis=1)) 
    df=df.assign(christmas=lambda df:df.apply(lambda row: 1 if row.event_name_1=="Christmas" 
                                                            or row.event_name_2=="Christmas" else 0,axis=1)) 
    
    df.drop(['event_type_1','event_type_2'],axis=1,inplace=True)
    
    return df