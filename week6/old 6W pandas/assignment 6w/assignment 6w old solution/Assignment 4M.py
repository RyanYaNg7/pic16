# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 13:06:28 2016

@author: matthaberland
"""

import time
import pandas as pd
import os
from pandas.tseries.offsets import DateOffset
t = time.time()

def round_time(time):
    sec_in_20_min = 20*60*1000
    return (time//sec_in_20_min)*sec_in_20_min
    
def process_file(filename):
    df = pd.read_csv(filename, names = ["Time","Inst","Cumu"])   
    df = df[df.Time.notnull()] 
    df.Time[0] = round_time(df.Time[0])   
    df = df.set_index("Time") 
    df.index = pd.to_datetime(df.index, unit = "ms", utc = True)    
    df = df.tz_convert("US/Eastern")
    delta = DateOffset(minutes = 20)
    df = df.asfreq(delta, method = "ffill")
    df["TOD"] = df.index.strftime("%A %H:%M")
    return df

dfs = []
files = os.listdir(os.getcwd())
for f in files:
    if f.endswith("csv"):
        dfs.append(process_file(f))
df = pd.concat(dfs)

dfgb = df.groupby("TOD")
df = dfgb.agg({"Inst": pd.Series.mean})
df.to_excel('output.xlsx', sheet_name='ThirstyAvgCount')

#print round_time(t)
#s = "2013-1-17-21-58-39.csv"
#df = process_file(s)
#print df