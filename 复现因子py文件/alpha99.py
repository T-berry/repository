# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 11:53:53 2018

@author: beleaf
"""

#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':5}
    if not param:
        param = defult_param
    
    alpha99 = dv.add_formula('alpha99', 
       "(-1*Rank(Covariance(Rank(close),Rank(volume),%s)))"%(param['t1'])
       , is_quarterly=False)
    
    return alpha99 