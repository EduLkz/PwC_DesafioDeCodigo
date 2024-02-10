numberPrefix = ["No", "no", "Nº", "nº", "n", "N"]
numberIndexes = []

def OrganizeAddress(address):
    address_splited = address.split(' ')
    number = ''

    number = findNumber(address_splited).replace(',', '')
    street = getAddress(address_splited).replace(',', '')
    final_address = '{\"' + street + '\", \"' + number + '\"}'

    print(final_address)


def findNumber(address):
    for index, part in enumerate(address):
        for p in numberPrefix:
            if(part == p):
                number = part + ' ' +address[index + 1]

                if(len(address) - 1 >= index + 2):
                    if(len(address[index + 2]) <= 1):
                        number += ' ' + address[index + 2]
                        numberIndexes.append(address[index + 2])

                numberIndexes.append(address[index])
                numberIndexes.append(address[index + 1])
                return number
            
    for index, part in enumerate(address):
        if len(part) < 6:
            count = 0
            
            for value in part:
                if( value.isdigit() ):
                    count += 1
            
            if(count >= len(part) - 1 and count > 0):
                number = ''
                
                number += part
                numberIndexes.append(part)
                
                if(len(address) - 1 >= index + 1):
                    if(len(address[index + 1]) <= 1):
                        number += ' ' + address[index + 1]
                        numberIndexes.append(address[index + 1])

                return number
    
    return 'Sem Numero'

def getAddress(address):
    finalAddress = ''
    
    addressCopy = address.copy()
    if len(numberIndexes) > 0:
         for number in numberIndexes:
            if number in addressCopy:
                addressCopy.remove(number)
            
    
    finalAddress = ' '.join(addressCopy)
    return finalAddress