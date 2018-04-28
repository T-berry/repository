# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 11:54:56 2018

@author: beleaf
"""

#type2  -  only use add_formula function with parameter
  
def run_formula(dv, param = None):
    defult_param = {'t1':21}
    if not param:
        param = defult_param
    
    Rstr504 = dv.add_formula('Rstr504', 
       "Decay_exp(Log(1+Delay(Return(close,1),%s))-Log(1+0.03/365),Pow(0.5,1/126),504)"%(param['t1'])
       , is_quarterly=False)
    
    return Rstr504