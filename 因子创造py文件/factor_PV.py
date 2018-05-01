# -*- coding: utf-8 -*-
"""
Created on Tue May  1 11:34:41 2018

@author: beleaf
"""

#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':34,'t2':34,'t3':34}
    if not param:
        param = defult_param
    
    factor_PV = dv.add_formula('factor_PV', 
           'Covariance(Rank(Return(close,%s)),Rank(volume/Ts_Mean(volume,%s)),%s)'%(param['t1'],param['t2'],param['t3']),
           is_quarterly=False)
    
    return factor_PV
