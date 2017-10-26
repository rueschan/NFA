dic = {}


def main():
    NAME = "input.txt"

    # fileName = raw_input("Ingrese el nombre del archivo:")
    file = open(NAME, 'r')
    file_write = open("output.txt", "w")

    for line in file:
        global dic
        dic = lineToDictionary(line)

        findTransitions()
        print dic

        # formatoBonito()
        formato = formatoBonito()
        sizeFormato = len(formato)
        count = 0
        c = 0
        for a in formato:
            # file_write.write()
            toprint = str(a).replace("'", "")  # .replace(" ","")

            sizePrint = len(toprint)
            final = ""
            if count == 0:
                final += "{"
            for i in toprint:

                if i == ")":
                    final += "),"
                else:
                    final += i
            count += 1
            file_write.write(final)
            # print dic

def formatoBonito():
    lista = []
    listaDfa = []
    for state in dic:
        destino = dic.get(state)
        destino_0 = "0", state, destino[0]
        lista.append(destino_0)
        destino_1 = "1", state, destino[1]
        lista.append(destino_1)

    strBuffer = ""
    for array_destiny in lista:
        for character_destiny in array_destiny[2]:
            strBuffer += character_destiny
        estadoNuevo = array_destiny[0], array_destiny[1], strBuffer
        listaDfa.append(estadoNuevo)
        strBuffer = ""

    return listaDfa

def lineToDictionary(line):
    dic = {}
    flag = True
    signal = -1
    origin = ""

    for letter in line:
        if letter.isdigit():
            flag = True
            signal = letter

            continue

        elif flag and letter.isalpha():
            flag = False
            origin = letter

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
    print "DICTO"
    print dic
    return dic


def findTransitions():

    print "FIND TRANSITION"

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
                print dic
                findTransitions()
                return
    return


main()
