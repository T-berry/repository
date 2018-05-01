# -*- coding: utf-8 -*-
"""
Created on Tue May  1 11:33:24 2018

@author: beleaf
"""

#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':5,'t2':5}
    if not param:
        param = defult_param
    
    BollDown_turnover = dv.add_formula('BollDown_turnover', 
           "Ts_Mean(turnover_ratio,%s)-2*StdDev(turnover_ratio,%s)"%(param['t1'],param['t2']),
           is_quarterly=False)
    
    return BollDown_turnover