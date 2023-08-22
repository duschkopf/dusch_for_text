# -*- coding: utf-8 -*-
"""
@author: roman.dushkov@gmail.com
"""

def translit(settings,     text): # last modified 23.07.2022
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
    # {text} to transliterate [str]
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
                mode = 'GOST'
                print(call_me_by_my_name + ' >> "mode" is set by default as "' + mode + '"')
            else:
                # 'GOST' 'ISO' 'telegram' 'ICAO' 'wiki' 'mosmetro'
# =============================================================================
#                 if True:
#                     automated_change = False # automated change switcher
#                     mode_new = '' # automatically changed missprints in {mode}
#                     if mode=='gost':
#                         mode_new = 'GOST'
#                         automated_change = True
#                     if mode=='iso':
#                         mode_new = 'ISO'
#                         automated_change = True
#                     if mode=='icao':
#                         mode_new = 'ICAO'
#                         automated_change = True
#                     if mode=='WIKI' or mode=='Wiki' or mode=='WIKIPEDIA' or mode=='Wikipedia' or mode=='wikipedia':
#                         mode_new = 'wiki'
#                         automated_change = True
#                     if mode=='MOSMETRO' or mode=='MosMetro' or mode=='Mosmetro' or mode=='Metro' or mode=='metro' or mode=='LEBEDEV' or mode=='Lebedev' or mode=='lebedev':
#                         mode_new = 'mosmetro'
#                         automated_change = True
#                     if automated_change:
#                         print(call_me_by_my_name + ' >> "' + mode + '" "mode" changed automatically into "' + mode_new + '"')
#                         mode = mode_new
# =============================================================================
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

        russian_abc        = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' # russian alphabet
        russian_vocals     = 'а    её  и     о    у       ы эюя'.replace(' ', '') # russian vocals
        russian_consonants = ' бвгд  жз йклмн прст фхцчшщ      '.replace(' ', '') # russian consonants
        russian_specials   = '                           ъ ь   '.replace(' ', '') # russian special symbols

        # simple rules for transliteration
        russian_simple = 'абвгд  зи  клмнопрстуф'.replace(' ', '')
        latin_simple   = 'abvgd  zi  klmnoprstuf'.replace(' ', '')

        # !!!
        # https://habr.com/ru/post/499574/
        # https://habr.com/ru/articles/265455/
        # rules for transliteration with dependences ({*} for more further rules)
        russian_more   = ['е','ё' ,'ж' ,  'и','й',  'х' ,'ц' ,  'ч' ,'ш' ,  'щ'   ,  'ъ' ,'ы' ,'ь',  'э', 'ю', 'я' ]
        latin_GOST     = ['e','yo','zh',  'i','j',  'x' ,'*' ,  'ch','sh',  'shh' ,  '``','y`','`',  'e`','yu','ya']
        latin_telegram = ['e','e' ,'j' ,  'i','i',  'h' ,'c' ,  'ch','sh',  'sc'  ,  ''  ,'y',''  ,  'e' ,'iu','ia']
        latin_ICAO     = ['e','e' ,'zh',  'i','i',  'kh','ts',  'ch','sh',  'shch',  'ie','y',''  ,  'e' ,'iu','ia']
        latin_wiki     = ['*','yo','zh',  'i','y',  'kh','ts',  'ch','sh',  'shch',  'y' ,'y','y' ,  'e' ,'yu','ya']
        latin_mosmetro = ['e','*' ,'zh',  '*','y',  'kh','*' ,  'ch','sh',  'sch' ,  '*' ,'*','*' ,  'e' ,'yu','ya']
        text_GOST      = '' # {text} tralsliterated by international standard (GOST 7.79-2000 or ISO 9:1995) (for reversible  transliteration)
        text_telegram  = '' # {text} tralsliterated by instruction of the Ministry of Communications (for the procedure for processing international telegrams)
        text_ICAO      = '' # {text} tralsliterated by the standard of the International Civil Aviation Organization (for documents usage)
        text_wiki      = '' # {text} tralsliterated by Wikipedia's scheme made on the basis of BGN/PCGN (for accurate phonetical transliteration)
        text_mosmetro  = '' # {text} tralsliterated by Moscow Metro's scheme made on the basis of Wikipedia/Yandex.Maps by Lebedev's Studio (for accurate visual transliteration)

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

                            # !!!
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