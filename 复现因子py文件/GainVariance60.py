# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 11:54:55 2018

@author: beleaf
"""

#type2  -  only use add_formula function with parameter

def cal_positive(df):
    return df[df>=0]
        
def run_formula(dv, param = None):
    defult_param = {'t1':60}
    if not param:
        param = defult_param
    
    GainVariance60 = dv.add_formula('GainVariance60', 
       "StdDev(CN(Return(close,1)),%s)^2"%(param['t1'])
       , is_quarterly=False,
       register_funcs={"CN":cal_positive})
    
    return GainVariance60