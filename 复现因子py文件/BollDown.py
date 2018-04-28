# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 11:58:54 2018

@author: beleaf
"""

#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':20,'t2':20}
    if not param:
        param = defult_param
    
    BollDown = dv.add_formula('BollDown_J', 
       "(Ts_Mean(close,%s)-2*StdDev(close,%s))"%(param['t1'],param['t2'])
       , is_quarterly=False)
    
    return BollDown