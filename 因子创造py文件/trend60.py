# -*- coding: utf-8 -*-
"""
Created on Tue May  1 11:30:20 2018

@author: beleaf
"""

#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':60}
    if not param:
        param = defult_param
    
    trend60 = dv.add_formula('trend60', 
           "Abs(Return(close,1))*Return(Ts_Mean(close,%s),1)"%(param['t1']),
           is_quarterly=False)
    
    return trend60