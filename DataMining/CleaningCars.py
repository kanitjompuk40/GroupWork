#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 10:38:46 2021

@author: mattwear
"""

import pandas as pd

### Data Cleaning Functions

# Getting rid of unecesarry columns

def remove_columns(df):
    columns = ["Unnamed: 0", "id", "image_url", "VIN", "region_url", "id", "model", "size"]
    df.drop(columns, axis=1, inplace=True)
    return(df)
