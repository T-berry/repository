# -*- coding: utf-8 -*-
"""
Created on Tue May  1 11:38:41 2018

@author: beleaf
"""

#type1  -  simplest type,only use add_formula function without parameter

def run_formula(dv):
    pca = dv.add_formula('pca', 
               "total_mv/TTM(tot_cur_assets)"
               , is_quarterly=True)
    return pca    