# -*- coding: utf-8 -*-
"""
Created on Tue May  1 11:40:17 2018

@author: beleaf
"""

#type3  -  

def run_formula(dv):
    import pandas as pd
    import numpy as np
    from jaqs_fxdayu.data.dataservice import LocalDataService
    dataview_folder = r'D:\my_data\量化云实习\data'
    ds = LocalDataService(fp=dataview_folder)
    rm=ds.index_daily(['000300.SH'], 20130101,  20180101,'trade_date,close')[0].set_index('trade_date')['close']
    
    Rm80=rm.pct_change(80)
    r80=dv.get_ts('close').pct_change(80)

    Index_var80=(Rm80.rolling(80).std())**2
    cov_r80=r80.rolling(80).cov(Rm80)
    beta80=cov_r80.apply(lambda x:x/Index_var80,axis=0)
    
    r_adj80=beta80.apply(lambda x:x*Rm80*100,axis=0)
    dv.append_df(r_adj80,'r_adj80')

    return r_adj80