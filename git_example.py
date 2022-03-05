# Primeiro precisamos importar a biblioteca do Easy SNMP
from easysnmp import Session

# Depois podemos criar uma sessao (session) SNMP para usar para todas as requisicoes
session = Session(hostname='localhost', community='public', version=2)


# Agora vamos fazer um SNMP GET REQUEST para descobrir o numero de interfaces do dispositivo gerenciado
ifNumber = session.get('ifNumber.0')


# Imprimir a quantidade de interfaces
print "Numero de interfaces", ifNumber.value


# Eh preciso converter o valor de ifNumber para inteiro porque o Easy SNMP nao faz isso por padrao
numInterfaces = int(ifNumber.value)

# Fazendo uma requisicao bulk com dois contadores in/out das interfaces de uma vez (repetindo conforme a quantidade de interfaces), isso vai retornar numInterfaces*2 objetos
countBulk = session.get_bulk(['ifInOctets', 'ifOutOctets'], 0, numInterfaces)


# Aqui vou definir duas listas (formalmente sao chamados de dicionarios) para armazenar os valores de contadores de cada interface
valifInOctets = {}
valifOutOctets = {}


# O nosso countBulk vai ter uma lista com numInterfaces*2 objetos, entao sera necessario repetir os comandos considerando a quantidade de interfaces (similar ao que foi feito no exemplo basico primeiro.py)
for i in range(numInterfaces):
# Os contadores in/out da interface i estarao na lista um apos o outro (posicoes i e i+1)
    ifInOctets = countBulk[i]
    ifOutOctets = countBulk[i+1]
# Convertendo os valores para inteiro
    valifInOctets[i] = int(ifInOctets.value)
    valifOutOctets[i] = int(ifOutOctets.value)
    print "Informacoes da Interface", i
    print "- In", valifInOctets[i], "(bytes)"
    print "- Out", valifOutOctets[i], "(bytes)"
