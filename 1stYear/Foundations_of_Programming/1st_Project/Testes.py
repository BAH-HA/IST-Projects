letras_minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letras_maiusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#1.2.1 Feito
def corrigir_palavra(string):
    i = 0
    while i < 26:
        seq_minmai = letras_minusculas[i] + letras_maiusculas[i]  # Duas letras ex.:'aA'
        seq_maimin = letras_maiusculas[i] + letras_minusculas[i]  # Duas letras ex.:'Qq'
        if seq_minmai in string:
            string = string.replace(seq_minmai,'')
        if seq_maimin in string:
            string = string.replace(seq_maimin,'')
        i += 1
        if i == 26:                                                                                                                 # verifica se apos o primeiro
            for c in range(26):                                                                                                     # ciclo ainda há surtos
                if letras_minusculas[c] + letras_maiusculas[c] in string or letras_maiusculas[c] + letras_minusculas[c] in string:  # de letras e repete caso haja
                    i = 0
    return string
                                                    ###print(corrigir_palavra('corrigirAVvaBbCcQdDiIq'))

#1.2.2 Feito
def eh_anagrama(string1,string2):
    if string1.upper() != string2.upper():
        return sorted(string1.upper()) == sorted(string2.upper()) #Coloca em ordem Alfabetica e verifica se sao iguais
    return False
#print(eh_anagrama('iGual', 'igual'))


#Funcao Auxiliar#
def verificar_string(string1):
    return type(string1) == str and all(x.isalpha() or x.isspace() for x in string1) and len(string1.split()) - 1 == string1.count(' ') and len(string1) != 0
                                                               # Verifica se a string tem mais que 1 espaco por intervalo de palavras
                                                               # se a string nao e vazia e se nao contem numeros ou caracteres especiais


#1.2.3 feito
def corrigir_doc(string):
    if verificar_string(string):
        lista_palavras = []
        lista_palavras_minusculas = []
        lista_palavras_final = []
        count = 0
        lista_anagramas = []
        for c in string.split():
            lista_palavras.append(corrigir_palavra(str(c)))                     #retira os surtos de letras e coloca os numa lista
            lista_palavras_minusculas.append(corrigir_palavra(str(c)).lower())  #retira os surtos de letras e coloca os numa lista com letras minusculas
        for c in lista_palavras_minusculas:
            if ''.join(sorted(c)) not in lista_anagramas or lista_palavras_minusculas.count(c) > 1:
                lista_anagramas.append(''.join(sorted(c)))                      #coloca os anagramas numa lista (todos minusculos)
                lista_palavras_final.append(lista_palavras[count])              #coloca a palavra correspondente ao index do anagrama na lista de palavras, na lista de palavras final
            count += 1
        return ' '.join(lista_palavras_final)                                   #retorna uma string com todas as palavras finais separadas por um espaco
    else:
         raise ValueError('corrigir_doc: argumento invalido')

#print(corrigir_doc('Programacao porgramacao e programacao'))

#2

#2.2.1 feito
num = [1,2,3,4,5,6,7,8,9]
def obter_posicao(char,inteiro):
    if inteiro in num and char in ['C','B','E','D']:
        if char == 'C':
            if 0 <= num.index(inteiro) - 3:
                return num[num.index(inteiro) - 3]
            else:
                return inteiro
        elif char == 'B':
            if num.index(inteiro) + 3 <= 8:
                return num[num.index(inteiro) + 3]
            else:
                return inteiro
        elif char == 'E':
            if inteiro == 1 or inteiro == 4 or inteiro == 7:
                return inteiro
            else:
                return num[num.index(inteiro) - 1]
        elif char == 'D':
            if inteiro == 3 or inteiro == 6 or inteiro == 9:
                return inteiro
            else:
                return num[num.index(inteiro) + 1]
    else:
        raise ValueError('obter_posicao: argumento invalido')

#print(obter_posicao('D',6))
#2.2.2 feito
def obter_digito(cadeia_char,inteiro):
    numero = inteiro
    for letra in cadeia_char:
        if inteiro in num and letra not in ['C', 'B', 'E', 'D']:
            raise ValueError('obter_digito: argumento invalido')
        else:
            numero = obter_posicao(letra,numero)
    return numero
#print(obter_digito('',5))
#2.2.3 feito
def obter_pin(tuplo):
    numero = 1
    pin_list = []
    if type(tuplo) != tuple:
        raise ValueError('obter_pin: argumento invalido')
    for palavra in tuplo:
        if palavra == '':
            raise ValueError('obter_pin: argumento invalido')
        for letra in palavra:
            if letra not in ['C', 'B', 'E', 'D'] or not (4 <= len(tuplo) <= 10) or type(tuplo) != tuple:
                raise ValueError('obter_pin: argumento invalido')
    for palavra in tuplo:
        for letra in palavra:
            if not letra.isalpha():
                raise ValueError('obter_pin: argumento invalido')
            numero = obter_posicao(letra,numero)
        pin_list.append(numero)
    pin_tuplo = tuple(pin_list)
    if pin_tuplo == ():
        raise ValueError('obter_pin: argumento invalido')
    return pin_tuplo
#print(obter_pin((1)))
#3
#3.2.1 feito
def eh_entrada(tuplo):
    return type(tuplo) == tuple and len(tuplo) == 3 and len(tuplo[0]) != 0 and all(x in letras_minusculas or x in '-' for x in tuplo[0]) and not tuplo[0].startswith('-') and not tuplo[0].endswith('-') and \
           len(tuplo[1]) == 7 and tuplo[1].startswith('[') and tuplo[1].endswith(']') and all(x in letras_minusculas for x in tuplo[1][1:6]) and \
           type(tuplo[2]) == tuple and len(tuplo[2]) >= 2 and all(type(x) == int and x > 0 for x in tuplo[2])

#print(eh_entrada((1)))

#Funcao Auxiliar#
def char_count(caraters):
    dicionario = {}
    for e in caraters:
        if e.isalpha():
            if e in dicionario.keys():
                dicionario[e] += 1
            else:
                dicionario[e] = 1
    return dicionario

#3.2.2 feito
def validar_cifra(cifra,cadeia):
    controlo_certo_list = []
    resultado_contagem = sorted(char_count(cifra).items(),key=lambda x: (-x[1],x[0]))
    for i in range(5):
        controlo_certo_list.append(resultado_contagem[i][0])
    controlo_certo_str = ''.join(controlo_certo_list)
    controlo_certo_str = '[' + controlo_certo_str + ']'
    return cadeia == controlo_certo_str
                                #print(validar_cifra('aaaaa-bbb-zx-yz-xy', '[abxyz]'))

#3.2.3 feito
def filtrar_bdb(lista):
    lista_final = []
    if type(lista) != list or lista == []:
        raise ValueError('filtrar_bdb: argumento invalido')
    for i in lista:
        if not eh_entrada(i):
            raise ValueError('filtrar_bdb: argumento invalido')
        if not validar_cifra(lista[lista.index(i)][0],lista[lista.index(i)][1]):
            lista_final.append(i)
    return lista_final

#bdb = []
    #('aaaaa-bbbbbbbbb-cccccccccccccc-fffffffffffffffff-e','[ddbae]',(10000,2000))]
#print(filtrar_bdb([('aaaaa-bbb-zx-yz-xy', '[abxyz]', (950, 300))]))

#4.2

#4.2.2 feito
def obter_num_seguranca(inteiros):
    inteiros_list = []
    for e in inteiros:
        if e > 0:
            inteiros_list.append(e)
    inteiros_list.sort()
    return inteiros_list[1]-inteiros_list[0]
#print(obter_num_seguranca((300,404000,-40,2)))

#4.2.3

def decifrar_texto(cifra,numero):
    nova_string = ''
    indice = 0
    for letra in cifra:
        if letra.isalpha():
            if indice % 2 == 0:
                if letras_minusculas.index(letra) + numero + 1 > 25:
                    x = (letras_minusculas.index(letra) + numero + 1) % 26         #Caso a soma do index da letra + o numero de controlo + 1 fique out o f index
                    nova_string += letras_minusculas[x]                            #eh retirado o excesso
                else:
                    nova_string += letras_minusculas[letras_minusculas.index(letra) + numero + 1]
            elif indice % 2 != 0:
                if letras_minusculas.index(letra) + numero - 1 > 25:              #Caso a soma do index da letra + o numero de controlo - 1 fique out o f index
                    x = (letras_minusculas.index(letra) + numero - 1) % 26        #eh retirado o excesso
                    nova_string += letras_minusculas[x]
                else:
                    nova_string += letras_minusculas[letras_minusculas.index(letra) + numero - 1]
        elif (cifra[indice]) == '-':
            nova_string += ' '
        indice += 1
    return nova_string
                            #print(decifrar_texto('nyccjoj-vfrex-ncalml', 404-50))
#4.2.4
def decifrar_bdb(lista):
    lista_final = []
    if type(lista) != list:
        raise ValueError('decifrar_bdb: argumento invalido')
    for entrada in lista:
        if not eh_entrada(entrada):
            raise ValueError('decifrar_bdb: argumento invalido')
        else:
            lista_final.append(decifrar_texto(lista[lista.index(entrada)][0],obter_num_seguranca(lista[lista.index(entrada)][2])))
    return lista_final

                    #bdb = [('qgfo-qutdo-s-egoes-wzegsnfmjqz', '[abcde]',(2223,424,1316,99)), ('lctlgukvzwy-ji-xxwmzgugkgw','[abxyz]', (2388, 367, 5999)), ('nyccjoj-vfrex-ncalml','[xxxxx]', (50, 404))]

                                                                        #print(decifrar_bdb(bdb))


#5.2.1
def eh_utilizador(utilizador):
    lista_chaves = list(utilizador.keys())
    lista_chaves_rule = list(utilizador['rule'])
    if type(utilizador) == dict and lista_chaves == ['name','pass','rule']:
            if len(utilizador['name']) != 0 and len(utilizador['pass']) != 0 and type(utilizador['rule'] == dict):
                if lista_chaves_rule == ['vals','char'] and type(utilizador['rule']['vals']) == tuple:
                    if len(utilizador['rule']['vals']) == 2 and utilizador['rule']['vals'][0] < utilizador['rule']['vals'][1]:
                        if utilizador['rule']['char'] in letras_minusculas and len(utilizador['rule']['char']) == 1:
                            return True
    return False

#print(eh_utilizador({'name':'bruce.wayne','pass':'mynameisbatman','rule':{'vals':(2,5),'char': 'a' }}))

#5.2.2
def eh_senha_valida(senha,dict_senha):
    count_vogais = 0
    count_consecutivas = 0
    for letra in senha:
        if letra in 'aeiou':
            count_vogais += 1
    for e in letras_minusculas:
        if e + e in senha:
            count_consecutivas += 1
    return dict_senha['vals'][0] <= senha.count(dict_senha['char']) <=  dict_senha['vals'][1] \
            and count_vogais > 2 and count_consecutivas > 0



#print(eh_senha_valida('caibeffgh', {'vals': (1, 3), 'char': 'b'}))

#5.2.3
def filtrar_senhas(lista):
    lista_final = []
    if lista == []:
        raise ValueError('filtrar_senhas: argumento invalido')
    for dictionary in lista:
        if not(type(dictionary) == dict) and not (eh_utilizador(dictionary)):
            raise ValueError('filtrar_senhas: argumento invalido')
        elif not (eh_senha_valida(lista[lista.index(dictionary)]['pass'],lista[lista.index(dictionary)]['rule'])):
            lista_final.append(dictionary['name'])
    return lista_final