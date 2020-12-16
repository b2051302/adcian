# -*- coding: UTF-8 -*-
import time
import binascii
def canonize(source):
    stop_symbols = '.,!?:;-\n\r()'
    stop_words = (u'это', u'как', u'так',
                  u'и', u'в', u'над',
                  u'к', u'до', u'не',
                  u'на', u'но', u'за',
                  u'то', u'с', u'ли',
                  u'а', u'во', u'от',
                  u'со', u'для', u'о',
                  u'же', u'ну', u'вы',
                  u'бы', u'что', u'кто',
                  u'он', u'она', u'оно',
                  u'они', u'по')
    return ([x for x in [y.strip(stop_symbols) for y in source.lower().split()] if x and (x not in stop_words)])

def getshingle(sym):
    out = []
    for i in range(len(sym) - (shingleLen - 1)):
        out.append(binascii.crc32(' '.join([x for x in sym[i:i + shingleLen]]).encode('utf-8')))

    return out

def compaire(sym1, sym2):
    same = 0
    for i in range(len(sym1)):
        if sym1[i] in sym2:
            same = same + 1

    return same * 2 / float(len(sym1) + len(sym2)) * 100

shingleLen = 3
def shinglelen():
    with open('test1.docx', 'r', encoding="utf-8", errors='ignore') as file1:
        with open('test2.docx', 'r', encoding="utf-8", errors='ignore') as file2:
            text1 = file1.read()
            text2 = file2.read()
    t1 = getshingle(canonize(text1))
    t2 = getshingle(canonize(text2))
    print(compaire(t1, t2), '%')
shinglelen()