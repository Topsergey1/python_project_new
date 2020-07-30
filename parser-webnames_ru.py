"""" Выводит в файл список 4-х значных доменов"""
import requests, bs4

ss = '0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m m o p q r s t u v w y z'
mas = ss.split(' ')
f = open(u'domains.txt', 'w')
print('Парсер запущен')
print('  ')
for q in mas:
    m = 0
    while (m<120):
        m = m + 1
        s = requests.get('https://www.webnames.ru/scripts/ru4let.pl?domain=' + q +'%25&page=' + str(m))
        b = bs4.BeautifulSoup(s.text, "html.parser")
        p = b.select('.noh a')
        for x in p:
            s = (x.getText().strip())
            f.write(s + '\n')
f.close()
print('Парсер завершил работу')

