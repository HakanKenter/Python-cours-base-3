# -*- coding: utf8 -*-

from msilib import sequence


mon_text = "voici mon texte"
ma_list = ["texte", "teSET", "texte"]
def find_word(elem):
    s = 0
    my_sequence = "texte"
    if(type(elem) == list):
        for word in elem:
        
            # une fois
            # if s == 0:  
                if my_sequence == word:
                    print(word)
                    print(elem.index(word))
                    s += 1
                else:
                   pass
    else:
        if my_sequence in elem:
            print(my_sequence)    
                

# find_word(mon_text);
find_word(ma_list);