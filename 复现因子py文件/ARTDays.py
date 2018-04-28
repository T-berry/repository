# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 11:59:00 2018

@author: beleaf
"""

#type1  -  simplest type,only use add_formula function without parameter
        
def run_formula(dv):
    ARTDays = dv.add_formula('ARTDays_J', 
               "(360*Ts_Mean(acct_rcv+notes_rcv-adv_from_cust,4))/TTM(oper_rev)"
               , is_quarterly=True)
    return ARTDays 