# -*- coding: utf-8 -*-
"""
Created on Tue May  1 11:28:24 2018

@author: beleaf
"""

#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':15,'t2':20}
    if not param:
        param = defult_param
    
    recover_s = dv.add_formula('recover_s', 
           "Delta(Ts_Min(close,%s),%s)"%(param['t1'],param['t2']),
           is_quarterly=False)
    
    return recover_s
