# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 11:54:53 2018

@author: beleaf
"""

#type1  -  simplest type,only use add_formula function without parameter

def run_formula(dv):
    alpha133 = dv.add_formula('alpha133', 
               "(((20-Ts_Argmax(high,20))/20) * 100 - ((20-Ts_Argmin(low,20))/20) * 100)"
               , is_quarterly=False)
    return alpha133