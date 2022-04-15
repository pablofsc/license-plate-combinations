# Gera uma lista de combinações de placas no formato AAA9A99 que formem palavras
# 29/09/2018

# Configurações do programa (mostrar ou não logs de adição ou recusa de palavras)
mostraradd = bool(True)
mostrarneg = bool(True)

# Leitura do dicionário de palavras
original = open('wordlist.txt', "r", encoding = "latin-1")
stringlist = (original.read()).split("\n")

# Variáveis
lista = open('placas.txt', 'w')
i = int
j = int(0)
numero = str
placa = str
placastr = str
placaf = str
elegivel = bool
n = int
motivo = str('Motivo: ')

# Início do algoritmo
for i in range(len(stringlist)):
    elegivel = True
    placastr = stringlist[i].upper()
    placa = list(placastr)

    if len(placastr) <= 7 and not ("-" in placastr):
        if len(placastr) >= 4:
            n = 3
            if placa[n] == 'O':
                placa[n] = '0'
            elif placa[n] == 'I':
                placa[n] = '1'
            elif placa[n] == 'Z':
                placa[n] = '2'
            elif placa[n] == 'E':
                placa[n] = '3'
            elif placa[n] == 'A':
                placa[n] = '4'
            elif placa[n] == 'S':
                placa[n] = '5'
            elif placa[n] == 'T':
                placa[n] = '7'
            else:
                elegivel = False
                motivo = 'Uma das letras não pode ser convertida para número.'

        if len(placastr) >= 6:
            n = 5
            if placa[n] == 'O':
                placa[n] = '0'
            elif placa[n] == 'I':
                placa[n] = '1'
            elif placa[n] == 'Z':
                placa[n] = '2'
            elif placa[n] == 'E':
                placa[n] = '3'
            elif placa[n] == 'A':
                placa[n] = '4'
            elif placa[n] == 'S':
                placa[n] = '5'
            elif placa[n] == 'T':
                placa[n] = '7'
            else:
                elegivel = False
                motivo = 'Uma das letras não pode ser convertida para número.'

        if len(placastr) == 7:
            n = 6
            if placa[n] == 'O':
                placa[n] = '0'
            elif placa[n] == 'I':
                placa[n] = '1'
            elif placa[n] == 'Z':
                placa[n] = '2'
            elif placa[n] == 'E':
                placa[n] = '3'
            elif placa[n] == 'A':
                placa[n] = '4'
            elif placa[n] == 'S':
                placa[n] = '5'
            elif placa[n] == 'T':
                placa[n] = '7'
            else:
                elegivel = False
                motivo = 'Uma das letras não pode ser convertida para número.'

    else:
        elegivel = False
        motivo = 'Palavra muito grande.'

    if elegivel:
        if len(placastr) == 2:
            placa.append('A')
        if len(placastr) <= 3:
            placa.append('9')
        if len(placastr) <= 4:
            placa.append('A')
        if len(placastr) <= 5:
            placa.append('9')
        if len(placastr) <= 6:
            placa.append('9')

        j = j + int(1)

        if len(str(j)) < 5:
            if len(str(j)) == 1:
                numero = '#0000' + str(j)
            elif len(str(j)) == 2:
                numero = '#000' + str(j)
            elif len(str(j)) == 3:
                numero = '#00' + str(j)
            elif len(str(j)) == 4:
                numero = '#0' + str(j)
        else:
            numero = '#' + str(j)

        placaf = str(placa)
        placaf = placaf.replace('[', '')
        placaf = placaf.replace(']', '')
        placaf = placaf.replace(',', '')
        placaf = placaf.replace("'", '')
        placaf = placaf.replace(' ', '')

        lista.write(numero + ' ' + placaf + ' ' + '(' + placastr +')'+ "\n")
        if mostraradd:
            print("Adicionado: " + numero, placaf, '(' + placastr + ')')
    else:
        if mostrarneg:
            print("Inelegível: #" + str(i) + ' - ' + placastr.lower() + '(' + str(len(placastr)) + ')' + ': ' + motivo)

print('\nPrograma conluído, ' + str(len(stringlist)) + ' palavras processadas e ' + str(j) + ' combinações encontradas.')

# Fim do algoritmo e fechamento dos arquivos de dicionário e lista final
lista.close()
original.close()
