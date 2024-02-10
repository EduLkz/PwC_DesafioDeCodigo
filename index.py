print('Entre endereço com dados contatenados: ')

address = input()
address_splited = address.split(' ')
number = 'NONE'

for index, part in enumerate(address_splited):
    if len(part) < 6:
        count = 0
        
        for value in part:
            if( value.isdigit() ):
                count += 1
        
        if(count >= len(part) - 1 and count > 0):
            number = ''

            if(index - 1 > 0 and len(address_splited[index - 1]) <= 2):
                number = address_splited[index - 1] + ' '
            
            number += part

            if(len(address_splited) <= index + 1 and len(address_splited[index + 1]) <= 2):
                number += ' ' + address_splited[index + 1]
            


print(number)