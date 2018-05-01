# -*- coding: utf-8 -*-
"""
Created on Tue May  1 11:37:38 2018

@author: beleaf
"""

def run_formula(dv, param = None):
    defult_param = {'t1':60}
    if not param:
        param = defult_param
    
    AD_hl60 = dv.add_formula('AD_hl60', 
           "Ts_Mean(Sign(Delta(close,1))*(high-low)*volume,%s)"%(param['t1']),
           is_quarterly=False)
    
    return AD_hl60