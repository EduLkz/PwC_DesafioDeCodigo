from Address import *;

print('Entre endereço com dados contatenados: ')

address = input()
address_splited = address.split(' ')
number = ''

number = findNumber(address_splited)
street = getAddress(address_splited)
final_address = {street, number}

print(final_address)