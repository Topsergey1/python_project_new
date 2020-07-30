"""" Сканер портов"""
import socket
print('Простейший сканер портов на Python')
print('   ')
host = input('Введите имя сайта или IP адрес:')
print('   ')
print('Ожидайте идес сканирование портов!')
print('-----------------------------------------')

for port in range(130, ):
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((host, port))
    except socket.error:
        pass
    else:
        s.close()
        print(host + ': ' + str(port) + ' порт активен')
print('-----------------------------------------')
print('Процесс завершен')
