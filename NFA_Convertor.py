#encoding: UTF-8

# Jose Antonio Malo de la Peña A01371454
# Rubén Escalante Chan A01370880

dic = {}
initialState = ""
indexes = ""


def main():

    while True:
        NAME = raw_input("Ingrese el nombre del archivo:")

        try:
            file_read = open(NAME, 'r')
            break
        except IOError:
            print "El archivo no se encuentra en el directorio. Ingrese un archivo valido..."

    file_write = open("output.txt", "w")


    for line in file_read:
        print "\nNFA:"
        print line
        global dic
        dic = lineToDictionary(line)

        findTransitions()

        formato = format()
        sizeFormato = len(formato)
        count = 0

        formato = sortInitialState(formato)

        print "DFA:"
        final = ""
        finished = False
        for a in formato:
            toprint = str(a).replace("'", "")

            final = ""
            if count == 0:
                final += "{"
            elif count == sizeFormato - 1:
                for i in toprint:
                    final += i
                    finished = True

            if not finished:
                for i in toprint:
                    if i == ")":
                        final += "),"
                    else:
                        final += i
                count += 1
                print final
                file_write.write(final + "\n")

        final += "}\n\n"
        print final
        file_write.write(final)


def sortInitialState(lista):

    pos = 0
    for a in lista:
        if a[1] == initialState:

            if pos == 0:
                temp = a
                lista[0] = temp
                pos += 1

            elif pos == 1:
                temp = a
                lista[1] = temp
                pos = -1

    return lista

def format():
    lista_diccionario = []
    lista_dfa = []
    for state in dic:
        destino = dic.get(state)
        global indexes
        if indexes in ["a", "b"]:
            destino_0 = "a", state, destino[0]
            lista_diccionario.append(destino_0)
            destino_1 = "b", state, destino[1]
            lista_diccionario.append(destino_1)
        elif indexes in ["0", "1"]:
            destino_0 = "0", state, destino[0]
            lista_diccionario.append(destino_0)
            destino_1 = "1", state, destino[1]
            lista_diccionario.append(destino_1)

    strBuffer = ""
    for array_destiny in lista_diccionario:
        for character_destiny in array_destiny[2]:
            strBuffer += character_destiny
        estadoNuevo = array_destiny[0], array_destiny[1], strBuffer
        lista_dfa.append(estadoNuevo)
        strBuffer = ""

    return lista_dfa


def lineToDictionary(line):
    dic = {}
    flag = True
    signal = ""
    origin = ""

    initial = True
    isKey = False
    for letter in line:

        if letter == "(":
            isKey = True
            continue

        if isKey:
            flag = True
            signal = letter
            isKey = False
            global indexes
            indexes = signal

            continue

        elif flag and letter.isalpha():
            flag = False
            origin = letter

            if initial:
                global initialState
                initialState = letter
                initial = False

            if not dic.has_key(origin):
                des = [[], []]
                dic[origin] = des

            continue

        elif letter.isalpha():
            if signal == "0" or signal == "a":
                temp = dic.get(origin)
                temp[0].append(letter)
                dic[origin] = temp
            else:
                temp = dic.get(origin)
                temp[1].append(letter)
                dic[origin] = temp
    return dic


def findTransitions():

    arr = dic.items()
    for state in arr:
        destiny = state[1]

        for half in destiny:
            key = ""
            for tag in half:
                key += tag

            if not dic.has_key(key) and key != "":
                des = [[], []]
                dic[key] = des
                temp = dic.get(key)

                for tag in half:
                    target = dic.get(tag)

                    s0 = target[0]
                    for i in s0:
                        if i not in temp[0]:
                            temp[0].append(i)

                    s1 = target[1]
                    for i in s1:
                        if i not in temp[1]:
                            temp[1].append(i)

                dic[key] = temp
                findTransitions()
                return
    return


main()
