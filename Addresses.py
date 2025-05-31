import os
from AddressOrganizer import *;

#print('Entre endereço com dados contatenados: ')
#address = input()

adresses = [
    #Casos Simples
    "Miritiba 339",
    "Babaçu 500",
    "Cambuí 804B",
    #Casos Intermediario
    "Rio Branco 23",
    "Quirino dos Santos 23 b",
    #Casos Complexos
    "4, Rue de la République",
    "100 Broadway Av",
    "Calle Sagasta, 26",
    "Calle 44 No 1991",
    #Casos Extras
    "Rua Iara n 236",
    "Av Taboão n320 b, ap 350",
    "Rua Lenita"
]

for address in adresses:
    OrganizeAddress(address)#

os.system('pause')