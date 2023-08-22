# -*- coding: utf-8 -*-
"""
@author: roman.dushkov@gmail.com
"""

def fragment_search(settings,     text,fragment): # last modified 21.07.2022
    # !!!
    my_name = 'fragment_search' # name of this function [str]
    '''

    This function finds {position} of {fragment} in {text},
    {case_sensitive} switch to take case of symbols into consideration

    '''
    # results
    number_of_fragments_tab = [] # number of appearences of {fragment} in {text} [list] of [int]
    position = [] # positions of symbols of {fragment} in {text} [list] of 0 and [str]
    # variables
    callname = settings[0] # name of a program from where this function is called [str]
    logger   = settings[1] # logging switcher [bool]
    case_sensitive = settings[2] # case sensitive switcher [bool]
    # {text} to search fragment in [str]
    # {fragment} to search in text [str] or [list] of [str]
    """
    text = 'Hello, my little pony world! OH MY LITTLE WORLD'
    fragment = '!'
    fragment = ['MY LITTLE', 'pony', 'WORLDWIDE']
    """
    # fool check
    if True:
        fool_check = False # parameter for checking invalid variables
        # callname
        if True:
            # [str]
            if isinstance(callname,str):
                call_me_by_my_name = callname + ' > ' + my_name # full function path
            else:
                print('UNKNOWN > ' + callname + ' >> insert "callname" in [str] format, ERROR')
                fool_check = True
        # logger
        if True:
            # [bool]
            if not isinstance(logger,bool):
                print(call_me_by_my_name + ' >> insert "logger" in [bool] format, ERROR')
                fool_check = True
        # !!!
        # case_sensitive
        if True:
            # [bool]
            if not isinstance(case_sensitive,bool):
                print(call_me_by_my_name + ' >> insert "case_sensitive" in [bool] format, ERROR')
                fool_check = True
        # !!!
        # text
        if True:
            # [str]
            if not isinstance(text,str):
                print(call_me_by_my_name + ' >> insert "text" in [str] format, ERROR')
                fool_check = True
            else:
                # empty
                if text=='':
                    print(call_me_by_my_name + ' >> insert "text" (can not be empty), ERROR')
                    fool_check = True
        # !!!
        # fragment
        if True:
            # [str] [list]
            if not (  isinstance(fragment,str) or isinstance(fragment,list)  ):
                print(call_me_by_my_name + ' >> insert "fragment" in [str] or [list] format, ERROR')
                fool_check = True
            # [list] of [str]
            if isinstance(fragment,list):
                for i in range(len(fragment)):
                    if not isinstance(fragment[i],str):
                        print(call_me_by_my_name + ' >> insert "fragment" as [list] of [str], ERROR')
                        if logger:
                            print(call_me_by_my_name + ' >> "' + str(fragment[i]) + '" is not [str]')
                        fool_check = True
    '''
    CORE
    '''
    # import libraries
    # !!!
    import sys
    if logger:
        print(call_me_by_my_name + ' >> import libraries, OK')
    # fool check resolution
    if fool_check:
        print(call_me_by_my_name + ' >> check input variables, ERROR')
        sys.exit()
    else:
        if logger:
            print(call_me_by_my_name + ' >> fool check, OK')
    # !!!
    if not fool_check:

        # initial formatting
        if True:
            fragment_tab = [] # array of fragments
            if isinstance(fragment,list):
                fragment_tab = fragment
            else: # [str]
                fragment_tab = [fragment]
            if logger:
                print(call_me_by_my_name + ' >> initialization, OK')

        # number of symbols in lines
        if True:
            L_text = len(text) # length of {text} [int]
            L_fragment_tab = [] # length of {fragment} [list] of [int]
            for i in range(len(fragment_tab)):
                L_fragment_tab.append(  len(fragment_tab[i])  )
            N_fragment = len(L_fragment_tab) # number of {fragment} to search

        # case considering
        if True:
            text_case = '' # {text} with case considering [str]
            fragment_case_tab = [] # {fragment} with case considering [list] of [str]
            if case_sensitive:
                text_case = text
                for i in range(len(fragment_tab)):
                    fragment_case_tab.append(  fragment_tab[i]  )
            else:
                text_case = text.lower()
                for i in range(len(fragment_tab)):
                    fragment_case_tab.append(  fragment_tab[i].lower()  )
            if logger:
                print(call_me_by_my_name + ' >> case considering, OK')

        # {fragment} search in {text}
        if True:
            fragments_positions_tab = [] # positions of {fragment} in {text} [list] of [int]
            for ii in range(len(text)):
                position.append(0)
            for i in range(N_fragment): # search through {fragment} list one by one
                frag = fragment_case_tab[i] # curent fragment [str]
                number_of_fragments_tab.append(0)
                N_frag = 0 # number of {frag} appearance [int]
                for j in range(L_text): # search through {text} symbol by symbol
                    ch_text = text_case[j] # curent symbol in {text} [str]
                    ch_frag = frag[0] # curent symbol in {frag} [str]
                    if ch_text == ch_frag: # first overlap
                        for k in range(len(frag)): # search through {frag} symbol by symbol
                            if (j+k)<L_text: # within range of {text}
                                if text_case[j+k] == frag[k]:
                                    if k==len(frag)-1: # end of {frag}
                                        N_frag = N_frag + 1 # new appearance of {frag}
                                        for ll in range(len(frag)): # add all symbols from {frag}
                                            fragments_positions_tab.append(  (j+k)  -  len(frag)  +  ll  +  1  )
                number_of_fragments_tab[i] = N_frag
                for jj in range(len(text)): # read through {text} symbol by symbol
                    for kk in range(len(fragments_positions_tab)): # read through appearances one by one
                        Num = fragments_positions_tab[kk] # current position of appearance
                        if jj==Num:
                            if position[jj]==0:
                                position[jj] = frag
            if logger:
                print(call_me_by_my_name + ' >> fragments position, OK')

# =============================================================================
#         # check if any {fragment} appears in {text}
#         if True:
#             fragment_appearence_tab = [] # number of appearences of {fragment} in {text} [list] of [bool]
#             any_appearance = False # in any {fragment} appears in {text}
#             for i in range(N_fragment):
#                 if fragment_case_tab[i] in text_case:
#                     fragment_appearence_tab.append(True)
#                     any_appearance = True
#                 else:
#                     fragment_appearence_tab.append(False)
#             if logger:
#                 if any_appearance:
#                     print(call_me_by_my_name + ' >> at least one fragment from ' + str(fragment) + ' is found, OK')
#                 else:
#                     print(call_me_by_my_name + ' >> no fragments from ' + str(fragment) + ' is found, OK')
# =============================================================================

        # check if {fragment} appears in {text}
        if True and len(number_of_fragments_tab)>0:
            if max(number_of_fragments_tab)<=0:
                # no appearances
                if logger:
                    print(call_me_by_my_name + ' >> no fragments from ' + str(fragment) + ' is found, OK')
            else:
                # at least one appearance
                if max(number_of_fragments_tab)>0:
                    if logger:
                        print(call_me_by_my_name + ' >> at least one fragment from ' + str(fragment) + ' is found, OK')
                # all appearances
                if min(number_of_fragments_tab)>0:
                    if logger:
                        print(call_me_by_my_name + ' >> every fragment from ' + str(fragment) + ' is found, OK')

        if logger:
            print(call_me_by_my_name + ' >> DONE.')

    func_out = [position,number_of_fragments_tab,     call_me_by_my_name]
    return func_out