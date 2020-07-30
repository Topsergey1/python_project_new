"""" Выводит в файл отсортированный список доменов"""
print('Начало сортировки')
f = open(u'domains.txt', 'r')
ff = open(u'domains2.txt', 'w')
str1 = '0123456789-'
glasnye = 'eyuioa'
for x in f:
    x = x.strip()
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
    if (not(a in '0123456789-')) and (not(b in '0123456789-')) and (not(c in '0123456789-')) and (not(d in '0123456789-')):
        aa = ''
        bb = ''
        cc = ''
        dd = ''
        if (a in 'eyuioa'):
            aa = 'g'
        else:
            aa = 's'
        if (b in 'eyuioa'):
            bb = 'g'
        else:
            bb = 's'
        if (c in 'eyuioa'):
            cc = 'g'
        else:
            cc = 's'
        if (d in 'eyuioa'):
            dd = 'g'
        else:
            dd = 's'
        xx = aa + bb + cc + dd
        print(xx)
        mas = ['gsgs', 'sgsg', 'sgss', 'ssgs']
        if (xx in mas):
            ff.write(x + '\n')
f.close()
ff.close()
print('---------------------')
print('Конец сортировки')