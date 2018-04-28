# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 11:46:03 2018

@author: beleaf
"""
   
#type2  -  only use add_formula function with parameter

def run_formula(dv, param = None):
    defult_param = {'t1':1,'t2':1,'t3':20}
    if not param:
        param = defult_param
    
    alpha84 = dv.add_formula('alpha84', 
       "Ts_Sum(If(close>Delay(close,%s),volume,If(close<Delay(close,%s),-volume,0)),%s)"%(param['t1'],param['t2'],param['t3'])
       , is_quarterly=False)
    
    return alpha84