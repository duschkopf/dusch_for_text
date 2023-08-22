# -*- coding: utf-8 -*-
"""
@author: roman.dushkov@gmail.com
"""

def case_change(settings,     text): # last modified 23.07.2022
    # !!!
    my_name = 'case_change' # name of this function [str]
    '''

    This function changes case of symbols in {text} via chosen {mode}

    '''
    # results
    text_out = text # text with changes symbols case [str]
    text_out_tab = [text] # array of all possible changes [list] of [str]
    N_symbols_changed = [] # positions of changes symbols [list] of [int]
    # variables
    callname = settings[0] # name of a program from where this function is called [str]
    logger   = settings[1] # logging switcher [bool]
    mode = settings[2] # mode [str] for case changing
    """
    mode = 'lower'
    mode = 'upper'
    mode = 'one title'
    mode = 'titles'
    mode = 'inverse'
    mode = 'numpad'
    mode = 'numpad_RU'
    mode = 'numpad_EN'
    mode = ''
    """
    # {text} to change case in [str]
    """
    text = 'Hello, my LITTLE world! I am here for the 2nd time'
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
        # mode
        if True:
            # [str]
            if not isinstance(mode,str):
                print(call_me_by_my_name + ' >> insert "mode" in [str] format, ERROR')
                fool_check = True
            if mode=='': # default mode
                # !!!
                mode = 'inverse'
                print(call_me_by_my_name + ' >> "mode" is set by default as "' + mode + '"')
            else:
                # 'lower' 'upper' 'inverse' 'one title' 'titles' 'numpad' 'numpad_RU' 'numpad_EN'
                if not (  mode=='lower' or mode=='upper' or mode=='inverse' or mode=='one title' or mode=='titles' or mode=='numpad' or mode=='numpad_RU' or mode=='numpad_EN'  ):
                    print(call_me_by_my_name + ' >> choose "mode" wisely, ERROR')
                    print(call_me_by_my_name + ' >> mode = "lower" to make all symbols minuscule (into lower case)')
                    print(call_me_by_my_name + ' >> mode = "upper" to make all symbols majuscule (into upper case)')
                    print(call_me_by_my_name + ' >> mode = "one title" to make first letter CAPITAL')
                    print(call_me_by_my_name + ' >> mode = "titles" to make first letters CAPITAL for all words')
                    print(call_me_by_my_name + ' >> mode = "inverse" to inverse all symbols (into opposite case)')
                    print(call_me_by_my_name + ' >> mode = "numpad" to change special numpad symbols into numbers')
                    print(call_me_by_my_name + ' >> mode = "numpad_RU" to change numbers into special numpad symbols on russian keyboard')
                    print(call_me_by_my_name + ' >> mode = "numpad_EN" to change numbers into special numpad symbols on english keyboard')
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

        # minuscule (into lower case)
        text_lower = text.lower()
        # majuscule (into upper case)
        text_upper = text.upper()

        # first letter CAPITAL
        text_title = text.capitalize()
        # first letters CAPITAL for all words
        text_titles = text.title()

        # inverse case
        text_inverse = ''
        for ch in text:
            if ch.islower():
                text_inverse = text_inverse + ch.upper()
            else:
                if ch.isupper():
                    text_inverse = text_inverse + ch.lower()
                else:
                    text_inverse = text_inverse + ch

        # numpad
        numpad_numbers = '1234567890'
        # !!!
        numpad_RU      = '!"№;%:?*()'
        numpad_EN      = '!@#$%^&*()'
        # symbols into numbers
        text_numpad    = '' # text with numbers instead of symbols
        if True:
            mapping = str.maketrans(numpad_EN,numpad_numbers)
            text_numpad = text.translate(mapping)
            mapping = str.maketrans(numpad_RU,numpad_numbers)
            text_numpad = text.translate(mapping)
        # numbers into symbols
        text_numpad_RU = '' # text with russian keyboard symbols instead of numbers
        text_numpad_EN = '' # text with english keyboard symbols instead of numbers
        if True:
            for ch in text:
                if ch in numpad_numbers:
                    j = 10 # out of range of {numpad_numbers}
                    for i in range(len(numpad_numbers)):
                        if ch==numpad_numbers[i]:
                            j = i
                    if j<10:
                        text_numpad_RU = text_numpad_RU + numpad_RU[j]
                        text_numpad_EN = text_numpad_EN + numpad_EN[j]
                else:
                    text_numpad_RU = text_numpad_RU + ch
                    text_numpad_EN = text_numpad_EN + ch

        # output text
        if mode=='lower':
            text_out = text_lower
        if mode=='upper':
            text_out = text_upper
        if mode=='one title':
            text_out = text_title
        if mode=='titles':
            text_out = text_titles
        if mode=='inverse':
            text_out = text_inverse
        if mode=='numpad':
            text_out = text_numpad
        if mode=='numpad_RU':
            text_out = text_numpad_RU
        if mode=='numpad_EN':
            text_out = text_numpad_EN
        text_out_tab = [text_lower,text_upper,  text_title,text_titles,  text_inverse,  text_numpad,text_numpad_RU,text_numpad_EN]

        # check if anything changed
        if text!=text_out:
            for i in range(len(text)):
                if text[i]!=text_out[i]:
                    N_symbols_changed.append(i)
                    if logger:
                        print(call_me_by_my_name + ' >> symbol "' + text[i] + '" changed into "' + text_out[i] + '" (position=' + str(i) + ')')
        else:
            if logger:
                print(call_me_by_my_name + ' >> no symbols changed')

        if logger:
            print(call_me_by_my_name + ' >> DONE.')

    func_out = [text_out,text_out_tab,  N_symbols_changed,     call_me_by_my_name]
    return func_out