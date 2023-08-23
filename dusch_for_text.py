# -*- coding: utf-8 -*-
"""
@author: roman.dushkov@gmail.com
"""

def translit(settings,     text):
    # !!!
    my_name = 'translit' # name of this function [str]
    '''

    This function transliterates {text} in chosen {mode}

    '''
    # results
    text_out = '' # transliterated text
    text_out_tab = [text] # array of all possible transliterations [list] of [str]
    
    # variables
    callname = settings[0] # name of a program from where this function is called [str]
    logger   = settings[1] # logging switcher [bool]
    mode = settings[2] # mode [str]
    """
    mode = 'GOST'
    mode = 'ISO'
    mode = 'telegram'
    mode = 'ICAO'
    mode = 'wiki'
    mode = 'mosmetro'
    mode = ''
    """
    text = text # {text} to transliterate [str]
    """
    text = 'Юзер, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю с Ципочкой из Обшаровки P.S. sticks and stones, love'
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
                mode = 'GOST'
                print(call_me_by_my_name + ' >> "mode" is set by default as "' + mode + '"')
            else:
                # 'GOST' 'ISO' 'telegram' 'ICAO' 'wiki' 'mosmetro'
                if not (  mode=='GOST' or mode=='ISO' or mode=='telegram' or mode=='ICAO' or mode=='wiki' or mode=='mosmetro'  ):
                    print(call_me_by_my_name + ' >> choose "mode" wisely, ERROR')
                    print(call_me_by_my_name + ' >> mode = "GOST" or "ISO" to use the international standard (GOST 7.79-2000 or ISO 9:1995) (for reversible  transliteration)')
                    print(call_me_by_my_name + ' >> mode = "telegram" to use the instruction of the Ministry of Communications (for the procedure for processing international telegrams)')
                    print(call_me_by_my_name + ' >> mode = "ICAO" to use the standard of the International Civil Aviation Organization (for documents usage)')
                    print(call_me_by_my_name + ' >> mode = "wiki" to use Wikipedia scheme made on the basis of BGN/PCGN (for accurate phonetical transliteration)')
                    print(call_me_by_my_name + ' >> mode = "mosmetro" to use Moscow Metro scheme made on the basis of Wikipedia/Yandex.Maps by Lebedev Studio (for accurate visual transliteration)')
                    fool_check = True
    
    '''
    CORE
    '''
    # import libraries
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
    # GUIDES
    
    # russian alphabet
    russian_abc        = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' # russian alphabet
    russian_vocals     = 'а    её  и     о    у       ы эюя'.replace(' ', '') # russian vocals
    russian_consonants = ' бвгд  жз йклмн прст фхцчшщ      '.replace(' ', '') # russian consonants
    russian_specials   = '                           ъ ь   '.replace(' ', '') # russian special symbols
    
    # rules for russian --> latin transliteration
    # simple rules
    russian_simple = 'абвгд  зи  клмнопрстуф'.replace(' ', '')
    latin_simple   = 'abvgd  zi  klmnoprstuf'.replace(' ', '')
    # rules with dependences ({*} for more further rules)
    russian_more   = ['е','ё' ,'ж' ,  'и','й',  'х' ,'ц' ,  'ч' ,'ш' ,  'щ'   ,  'ъ' ,'ы' ,'ь',  'э', 'ю', 'я' ]
    # https://habr.com/ru/articles/265455/
    latin_GOST     = ['e','yo','zh',  'i','j',  'x' ,'*' ,  'ch','sh',  'shh' ,  '``','y`','`',  'e`','yu','ya']
    text_GOST      = '' # {text} tralsliterated by international standard (GOST 7.79-2000 or ISO 9:1995) (for reversible  transliteration)
    # https://habr.com/ru/post/499574/
    latin_telegram = ['e','e' ,'j' ,  'i','i',  'h' ,'c' ,  'ch','sh',  'sc'  ,  ''  ,'y',''  ,  'e' ,'iu','ia']
    latin_ICAO     = ['e','e' ,'zh',  'i','i',  'kh','ts',  'ch','sh',  'shch',  'ie','y',''  ,  'e' ,'iu','ia']
    latin_wiki     = ['*','yo','zh',  'i','y',  'kh','ts',  'ch','sh',  'shch',  'y' ,'y','y' ,  'e' ,'yu','ya']
    latin_mosmetro = ['e','*' ,'zh',  '*','y',  'kh','*' ,  'ch','sh',  'sch' ,  '*' ,'*','*' ,  'e' ,'yu','ya']
    text_telegram  = '' # {text} tralsliterated by instruction of the Ministry of Communications (for the procedure for processing international telegrams)
    text_ICAO      = '' # {text} tralsliterated by the standard of the International Civil Aviation Organization (for documents usage)
    text_wiki      = '' # {text} tralsliterated by Wikipedia's scheme made on the basis of BGN/PCGN (for accurate phonetical transliteration)
    text_mosmetro  = '' # {text} tralsliterated by Moscow Metro's scheme made on the basis of Wikipedia/Yandex.Maps by Lebedev's Studio (for accurate visual transliteration)

    if not fool_check:
        # transliteration
        for i in range(len(text)):
            ch_to_transliterate = text[i] # symbol to transliterate
            ch_to_transliterate_low = ch_to_transliterate.lower() # symbol to transliterate in lower case

            if ch_to_transliterate_low in russian_abc: # any russian symbol

                if ch_to_transliterate_low in russian_simple: # russian symbol with simple rule for transliteration
                    mapping = str.maketrans(russian_simple,latin_simple)
                    # transliterated symbol
                    ch_new = ch_to_transliterate_low.translate(mapping) # changed symbol
                    ch_GOST     = ch_new
                    ch_telegram = ch_new
                    ch_ICAO     = ch_new
                    ch_wiki     = ch_new
                    ch_mosmetro = ch_new
                else:
                    for j in range(len(russian_more)):
                        if ch_to_transliterate_low == russian_more[j]:
                            ch_GOST     = latin_GOST[j]
                            ch_telegram = latin_telegram[j]
                            ch_ICAO     = latin_ICAO[j]
                            ch_wiki     = latin_wiki[j]
                            ch_mosmetro = latin_mosmetro[j]

                            # symbols around
                            if i>0:
                                ch_before = text[i-1].lower() # symbol before current one
                            else:
                                ch_before = ''
                            if i<(len(text)-1):
                                ch_after = text[i+1].lower() # symbol after current one
                            else:
                                ch_after = ''
                            if i<(len(text)-2):
                                ch_afterafter = text[i+2].lower() # symbol after after current one
                            else:
                                ch_afterafter = ''

                            # GOST 7.79-2000 (ISO 9:1995)
                            if ch_GOST=="*":
                                if russian_more[j]=='ц':
                                    ch_GOST = 'cz'
                                    if ch_after in 'еийы':
                                        ch_GOST = 'c'
                            if mode=='GOST' or mode=='ISO':
                                if logger:
                                    print(call_me_by_my_name + ' >> symbol "' + russian_more[j] + '" transliterated as ' + ch_GOST + '", OK')
                            # Wikipedia
                            if ch_wiki=="*":
                                if russian_more[j]=='е':
                                    ch_wiki = 'e'
                                    if ch_before in russian_vocals or ch_before in russian_specials or ch_before=="" or ch_before==" ":
                                        ch_wiki = 'ye'
                                if russian_more[j]=='ъ':
                                    ch_wiki = 'y'
                                    if ch_after in 'еёюя' or ch_before=="" or ch_before==" ":
                                        ch_GOST = ''
                                if russian_more[j]=='ь':
                                    ch_wiki = 'y'
                                    if ch_after in 'еёюя' or ch_after in russian_consonants or ch_before=="" or ch_before==" " or ch_after=="" or ch_after==" ":
                                        ch_wiki = ''
                            if mode=='wiki':
                                if logger:
                                    print(call_me_by_my_name + ' >> symbol "' + russian_more[j] + '" transliterated as ' + ch_wiki + '", OK')
                            # MosMetro
                            if ch_mosmetro=="*":
                                if russian_more[j]=='ё':
                                    ch_mosmetro = 'e'
                                    if ch_after in russian_specials:
                                        ch_mosmetro = 'yo'
                                if russian_more[j]=='ц':
                                    ch_mosmetro = 'ts'
                                    if ch_before == 'т':
                                        ch_mosmetro = 's'
                                if russian_more[j]=='ъ':
                                    ch_mosmetro = ''
                                    if ch_after in 'аеиоуэ':
                                        ch_mosmetro = 'y'
                                if russian_more[j]=='ь':
                                    ch_mosmetro = ''
                                    if ch_after in 'аеиоуэ':
                                        ch_mosmetro = 'y'
                                # endings
                                if russian_more[j]=='ы':
                                    ch_mosmetro = 'y'
                                    if ch_after=='й' and (  ch_afterafter=='' or ch_afterafter==' '  ):
                                        ch_mosmetro = ''
                                if russian_more[j]=='и':
                                    ch_mosmetro = 'i'
                                    if ch_after=='й' and (  ch_afterafter=='' or ch_afterafter==' '  ):
                                        ch_mosmetro = ''
                            if mode=='mosmetro':
                                if logger:
                                    print(call_me_by_my_name + ' >> symbol "' + russian_more[j] + '" transliterated as ' + ch_mosmetro + '", OK')
            else:
                ch_old = ch_to_transliterate # symbol with no change
                ch_GOST     = ch_old
                ch_telegram = ch_old
                ch_ICAO     = ch_old
                ch_wiki     = ch_old
                ch_mosmetro = ch_old

            # case
            if ch_to_transliterate.isupper():
                ch_GOST     = ch_GOST.upper()
                ch_telegram = ch_telegram.upper()
                ch_ICAO     = ch_ICAO.upper()
                ch_wiki     = ch_wiki.upper()
                ch_mosmetro = ch_mosmetro.upper()

            # transliterated text
            text_GOST     = text_GOST     + ch_GOST
            text_telegram = text_telegram + ch_telegram
            text_ICAO     = text_ICAO     + ch_ICAO
            text_wiki     = text_wiki     + ch_wiki
            text_mosmetro = text_mosmetro + ch_mosmetro

        # output text
        if mode=='GOST' or mode=='ISO':
            text_out = text_GOST
        if mode=='telegram':
            text_out = text_telegram
        if mode=='ICAO':
            text_out = text_ICAO
        if mode=='wiki':
            text_out = text_wiki
        if mode=='mosmetro':
            text_out = text_mosmetro
        text_out_tab = [text_GOST,text_telegram,text_ICAO,text_wiki,text_mosmetro]

        # check if nothing changed
        if text==text_out:
            if logger:
                print(call_me_by_my_name + ' >> no letters tramsliterated')

        if logger:
            print(call_me_by_my_name + ' >> DONE.')

    func_out = [text_out,text_out_tab,     call_me_by_my_name]
    return func_out



def fragment_search(settings,     text,fragment):
    # !!!
    my_name = 'fragment_search' # name of this function [str]
    '''

    This function finds position of {fragment} in {text}, could be {case_sensitive} or not

    '''
    # results
    number_of_fragments_tab = [] # number of appearences of {fragment} in {text} [list] of [int]
    position = [] # positions of symbols of {fragment} in {text} [list] of 0 and [str]
    
    # variables
    callname = settings[0] # name of a program from where this function is called [str]
    logger   = settings[1] # logging switcher [bool]
    case_sensitive = settings[2] # case sensitive switcher [bool]
    text = text # {text} to search {fragment} in [str]
    """
    text = 'Hello, my little pony world! OH MY LITTLE WORLD'
    """
    fragment = fragment # {fragment} to search in text [str] or [list] of [str]
    """
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
        # case_sensitive
        if True:
            # [bool]
            if not isinstance(case_sensitive,bool):
                print(call_me_by_my_name + ' >> insert "case_sensitive" in [bool] format, ERROR')
                fool_check = True
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



def case_change(settings,     text):
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
    text = text # {text} to change case in [str]
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
    # GUIDES
    
    # numpad symbols
    numpad_numbers = '1234567890'
    numpad_RU      = '!"№;%:?*()'
    numpad_EN      = '!@#$%^&*()'
    
    if not fool_check:

        # all symbols change
        # minuscule
        text_lower = text.lower()
        # majuscule
        text_upper = text.upper()

        # first symbol CAPITAL change
        # for sentence
        text_title = text.capitalize()
        # for all words
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
                    
        # symbols into numbers and vice versa
        text_numpad    = '' # text with numbers instead of symbols
        if True:
            mapping = str.maketrans(numpad_EN,numpad_numbers)
            text_numpad = text.translate(mapping)
            mapping = str.maketrans(numpad_RU,numpad_numbers)
            text_numpad = text.translate(mapping)
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