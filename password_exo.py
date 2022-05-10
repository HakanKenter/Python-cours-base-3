# -*- coding: utf-8 -*-

test_str = "GeeksForGeeKs"
# def NbCMin(mystring):
#     res = [char for char in mystring if char.islower()] 
#     print(len(res)) 
# NbCMin(test_str)


# def NbCMax(mystring):
#     res = [char for char in mystring if char.isupper()] 
#     print(len(res)) 
# NbCMax(test_str)
    
    
# def NbCAlpha(mystring):
#     res = [char for char in mystring if not char.isalpha()] 
#     print(len(res)) 
# NbCAlpha(test_str)

def NbcMin(passe):
    nb = 0
    for i in passe:
        if 'a' <= i <= 'z':
            nb += 1
    return nb
 
# print(NbcMin(test_str))
def NbcMaj(passe):
    nb = 0
    for i in passe:
        if 'A' <= i <= 'Z':
            nb += 1
    return nb
 
def NbcAlpha(passe):
    return len(passe)-NbcMaj(passe)-NbcMin(passe)

def longMaj(passe):
    d = 0
    s = 0
    i = 0
    while i < len(passe):
        if 'A' < passe[i] < 'Z':
            s += 1
        else:
            if s > d:
                d = s
                s = 0
        i += 1
 
    return d
 
 
def longMin(passe):
    d = 0
    s = 0
    i = 0
    while i < len(passe):
        if 'a' < passe[i] < 'z':
            s += 1
        else:
            if s > d:
                d = s
                s = 0
        i += 1
 
    return d
 
 
def score(password):
    bonus = (len(password)-NbcMin(password))*3+(len(password) - NbcMaj(password))*2+(len(password)-NbcAlpha(password))*5
    penalites = longMaj(password)*3+longMin(password)*2
    val = bonus-penalites
    if val < 20:
        print('Très faible')
    elif val < 40:
        print('Faible')
    elif val < 80:
        print('Fort')
    else:
        print('Très fort')
 
 
pas = "P@SI_promo2016"
score(pas) 
