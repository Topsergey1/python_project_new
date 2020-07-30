"""" Выводит на печать запрошенную веб страницу"""
import requests, bs4
data = requests.get('https://webfanat.com')
print(data.text)



