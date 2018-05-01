# -*- coding: utf-8 -*-
"""
Created on Tue May  1 11:25:03 2018

@author: beleaf
"""

#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':120,'t2':120}
    if not param:
        param = defult_param
    
    recover_l = dv.add_formula('recover_l', 
           "(close-Ts_Min(close,%s))/Ts_Min(close,%s)"%(param['t1'],param['t2']),
           is_quarterly=False)
    
    return recover_l