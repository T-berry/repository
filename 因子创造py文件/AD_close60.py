# -*- coding: utf-8 -*-
"""
Created on Tue May  1 11:36:26 2018

@author: beleaf
"""

def run_formula(dv, param = None):
    defult_param = {'t1':60}
    if not param:
        param = defult_param
    
    AD_close60 = dv.add_formula('AD_close60', 
           "Ts_Mean(Sign(close-open)*close*volume,%s)"%(param['t1']),
           is_quarterly=False)
    
    return AD_close60