    {logger} [boolean] --> shows logging while exploiting the code (if True)

>> translit

This function transliterates {text} in chosen {mode}
    
    {text} [str] --> text to transliterate
    {mode} [str] --> different ways of transliteration
            "GOST" or "ISO" to use the international standard (GOST 7.79-2000 or ISO 9:1995) (for reversible transliteration)
            "telegram" to use the instruction of the Ministry of Communications (for the procedure for processing international telegrams)
            "ICAO" to use the standard of the International Civil Aviation Organization (for documents usage)
            "wiki" to use Wikipedia scheme made on the basis of BGN/PCGN (for accurate phonetical transliteration)
            "mosmetro" to use Moscow Metro scheme made on the basis of Wikipedia/Yandex.Maps by Lebedev Studio (for accurate visual transliteration)
            (default) "" == 'GOST'

>> fragment_search

This function finds {position} of {fragment} in {text}, could be {case_sensitive} or not
    
    {text} [str] --> {text} to search {fragment} in [str]
    {fragment} [str] or [list] of [str] --> {fragment} to search in text
    {case_sensitive} [bool] --> taking case of symbols into consideration (if True)

>> case_change

This function changes case of symbols in {text} via chosen {mode}
    
    {text} [str] --> text to change case in
    {mode} [str] --> mode for case changing
            "lower" to make all symbols minuscule (into lower case)
            "upper" to make all symbols majuscule (into upper case)
            "one title" to make first letter CAPITAL
            "titles" to make first letters CAPITAL for all words
            "inverse" to inverse all symbols (into opposite case)
            "numpad" to change special numpad symbols into numbers
            "numpad_RU" to change numbers into special numpad symbols on russian keyboard
            "numpad_EN" to change numbers into special numpad symbols on english keyboard
            (default) "" == 'inverse'
