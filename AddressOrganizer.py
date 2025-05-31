numberPrefix = ["No", "no", "Nº", "nº", "n", "N"]                       #Possiveis prefixos para o numero
numberArray = []

def OrganizeAddress(address):
    address_splited = address.replace(',', '').split(' ')                              #Separa o endereço de entrada em um Array

    num = findNumber(address_splited).replace(',', '')               #Encontra o numero e remove virgulas caso tenha
    rua = getAddress(address_splited).replace(',', '')               #Pega o endereço e remove virgulas caso tenha
    solucao = '{\"logradouro\":\"' + rua + '\",\"numero\":\"'+ num + '\"}'          #Formatação da saida

    print(solucao)


def findNumber(address):                                                #Encontra o numero do endereço
    for index, part in enumerate(address):
        for p in numberPrefix:                                          #Verifica a existencia de um Prefixo

            if(part == p):                                              #Caso encontre um prefixo, pega o numero seguido
                number = part + ' ' +address[index + 1]

                if len(address) - 1 >= index + 2:                       #Verifica se o numero possui um sufixos
                    if len(address[index + 2]) <= 1:
                        number += ' ' + address[index + 2]
                        numberArray.append(address[index + 2])          #Adiciona o sufixo ao array de numeros

                numberArray.append(address[index])                      #Adiciona o prefixo e o numero ao array de index
                numberArray.append(address[index + 1])
                return number                                           #Retorna numero final
            
    for index, part in enumerate(address):                              #Caso não ache o prefixo, faz a busca pelo numero avulso
        if len(part) < 6:                                               #limita a numeros de 5 digitos
            count = 0
            
            for value in part:
                if value.isdigit() :                                    #Verifica se a variavel é um numero
                    count += 1                                          #Diz o numero de digitos da que são numeros
            
            if(count >= len(part) - 1 and count > 0):                   #Caso tenha menos numeros ou uma quantidade igual ao tamanho do valor inicial, é considerado numero
                number = ''                                             #Menos numeros são considerados para caso de um prefixo ou sufixos junto ao numero. Ex: "24B"
                
                number += part
                numberArray.append(part)                                #Adiciona o numero ao array de numeros
                
                if len(address) - 1 >= index + 1 :                      #Veridica a existencia de sufixos avulsos
                    if len(address[index + 1]) <= 1 :
                        number += ' ' + address[index + 1]
                        numberArray.append(address[index + 1])

                return number                                           #Retorna o numero final
    
    return 'Sem Numero'                                                 #Caso numero não seja encontrado, é retornado o valor "Sem numero"

def getAddress(address):                                                #Separa a rua do numero
    finalAddress = ''
    
    addressCopy = address.copy()                                        #Cria uma copia do array para evitar possiveis erros ao alterar a variavel inicial
    if len(numberArray) > 0:
         for number in numberArray:                                     #Pega cada informação do array dos numeros
            if number in addressCopy:
                addressCopy.remove(number)                              #Remove o numero, e caso exista, prefixo e sufixo
            
    
    finalAddress = ' '.join(addressCopy)
    return finalAddress                                                 #Retorna o endereço final
