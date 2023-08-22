# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 16:22:28 2023

@author: Duschkopf
"""

callname = 'lets work with text' # name of a program from where this function is called [str]
logger   = True # logging switcher [bool]



import dusch_for_text__translit

text = 'Юзер, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю с Ципочкой из Обшаровки P.S. sticks and stones, love'

mode = 'mosmetro' # mode [str]
settings = [callname, logger, mode]
[text_out,text_out_tab,     call_me_by_my_name] = dusch_for_text__translit.translit(settings,     text)



import dusch_for_text__fragment_search

text = 'Hello, my little pony world! OH MY LITTLE WORLD'
fragment = '!'
fragment = ['MY LITTLE', 'pony', 'WORLDWIDE']

case_sensitive = True # case sensitive switcher [bool]
settings = [callname, logger, case_sensitive]
[position,number_of_fragments_tab,     call_me_by_my_name] = dusch_for_text__fragment_search.fragment_search(settings,     text,fragment)



import dusch_for_text__case_change

text = 'Hello, my LITTLE world! I am here for the 2nd time'

mode = ''
settings = [callname, logger, mode]
[text_out,text_out_tab,  N_symbols_changed,     call_me_by_my_name] = dusch_for_text__case_change.case_change(settings,     text)