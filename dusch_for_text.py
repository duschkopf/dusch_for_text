# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 16:22:28 2023

@author: Duschkopf
"""
import dusch_for_text__translit
callname = 'lets work with text' # name of a program from where this function is called [str]
logger   = True # logging switcher [bool]


text = 'Юзер, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю с Ципочкой из Обшаровки P.S. sticks and stones, love'
mode = 'mosmetro' # mode [str]
settings = [callname, logger, mode]

[text_out,text_out_tab,     call_me_by_my_name] = dusch_for_text__translit.translit(settings,     text)