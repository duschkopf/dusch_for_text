# -*- coding: utf-8 -*-
callname = 'how2_text' # name of a program from where this function is called [str]
logger   = True # logging switcher [bool]
import dusch_for_text



text = 'Юзер, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю с Ципочкой из Обшаровки P.S. sticks and stones, love'

mode = 'mosmetro' # mode [str]
settings = [callname, logger, mode]
[text_out,text_out_tab,     call_me_by_my_name] = dusch_for_text.translit(settings,     text)



text = 'Hello, my little pony world! OH MY LITTLE WORLD'
fragment = '!'
fragment = ['MY LITTLE', 'pony', 'WORLDWIDE']

case_sensitive = False # case sensitive switcher [bool]
settings = [callname, logger, case_sensitive]
[position,number_of_fragments_tab,     call_me_by_my_name] = dusch_for_text.fragment_search(settings,     text,fragment)



text = 'Hello, my LITTLE world! I am here for the 2nd time'

mode = ''
settings = [callname, logger, mode]
[text_out,text_out_tab,  N_symbols_changed,     call_me_by_my_name] = dusch_for_text.case_change(settings,     text)
