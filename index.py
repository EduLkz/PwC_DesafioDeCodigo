from Address import *;

print('Entre endereço com dados contatenados: ')

address = input()
address_splited = address.split(' ')
number = 'NONE'

number = findNumber(address_splited)


print(number)