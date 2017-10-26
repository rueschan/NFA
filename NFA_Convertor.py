dic = {}
initialState = ""


def main():
    NAME = "input.txt"

    # fileName = raw_input("Ingrese el nombre del archivo:")
    file = open(NAME, 'r')
    file_write = open("output.txt", "w")

    for line in file:
        global dic
        dic = lineToDictionary(line)

        findTransitions()

        # formatoBonito()
        formato = format()
        sizeFormato = len(formato)
        count = 0
        c = 0

        formato = sortInitialState(formato)

        final = ""
        finished = False
        for a in formato:
            # file_write.write()
            toprint = str(a).replace("'", "")  # .replace(" ","")

            sizePrint = len(toprint)
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
                file_write.write(final)

            print final

        final += "}"
        file_write.write(final)


def sortInitialState(lista):

    pos = 0
    for a in lista:
        if a[1] == initialState:

            if pos == 0:
                temp = a
                a = lista[0]
                lista[0] = temp
                pos += 1

            elif pos == 1:
                temp = a
                a = lista[1]
                lista[1] = temp
                pos = -1

    return lista

def format():
    lista_diccionario = []
    lista_dfa = []
    for state in dic:
        destino = dic.get(state)
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
    signal = -1
    origin = ""

    initial = True
    for letter in line:
        if letter.isdigit():
            flag = True
            signal = letter

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
            if signal == "0":
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
    # print arr
    for state in arr:
        destiny = state[1]
        # print destiny

        for half in destiny:
            key = ""
            for tag in half:
                key += tag

            # print key
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
