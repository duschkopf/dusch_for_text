there are 3 functional variables:

'logger' [boolean] --> shows logging while exploiting the code (if True)
'text' [str] --> text to tranliterate
'mode' [str] --> different ways of transliteration:
  "GOST" or "ISO" to use the international standard (GOST 7.79-2000 or ISO 9:1995) (for reversible transliteration)
  "telegram" to use the instruction of the Ministry of Communications (for the procedure for processing international telegrams)
  "ICAO" to use the standard of the International Civil Aviation Organization (for documents usage)
  "wiki" to use Wikipedia scheme made on the basis of BGN/PCGN (for accurate phonetical transliteration)
  "mosmetro" to use Moscow Metro scheme made on the basis of Wikipedia/Yandex.Maps by Lebedev Studio (for accurate visual transliteration)
