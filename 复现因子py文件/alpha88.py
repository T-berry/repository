# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 11:52:28 2018

@author: beleaf
"""

#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':20,'t2':20}
    if not param:
        param = defult_param
    
    alpha88 = dv.add_formula('alpha88', 
       "((close-Delay(close,%s))/Delay(close,%s))*100"%(param['t1'],param['t2'])
       , is_quarterly=False)
    
    return alpha88 