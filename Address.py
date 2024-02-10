numberPrefix = ["No", "no", "Nº", "nº", "n", "N"]
numberIndexes = []

def findNumber(address):
    for index, part in enumerate(address):
        for p in numberPrefix:
            #print(part, p)
            if(part == p):
                number = part + ' ' +address[index + 1]
                numberIndexes.append(index)
                numberIndexes.append(index + 1)
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
                numberIndexes.append(index)
                
                
                print(len(address), index)
                if(len(address) >= index + 1):
                    if(len(address[index + 1]) <= 2):
                        number += ' ' + address[index + 1]
                        numberIndexes.append(index + 1)

                return number