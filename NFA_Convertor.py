dic = {}


def main():
    NAME = "input.txt"
    ALPHABET = {"0", "1"}

    # fileName = raw_input("Ingrese el nombre del archivo:")
    file = open(NAME, 'r')

    for line in file:
        # dic = {}
        #
        # print line
        # transition = []
        # destiny = []
        # state = []
        # flag = True
        # signal = -1
        # origin = ""
        # for letter in line:
        #     if letter in ALPHABET:
        #         # state.append(destiny)
        #         # transition.append(state)
        #
        #         # RESET
        #         flag = True
        #         state = []
        #         destiny = []
        #         # RESET./
        #
        #         # state.append(letter)
        #         signal = letter
        #         # print ("signo " + letter)
        #         continue
        #
        #     elif (flag and letter.isalpha()):
        #         flag = False
        #         # state.append(letter)
        #         origin = letter
        #         # print ("origen " + letter)
        #
        #         # Agregar
        #         # exists = False
        #         # for tran in transition:
        #         #     if tran[0] == signal and tran[1] == origin:
        #         #         exists = True
        #         #
        #         # if not exists:
        #         #     state.append(signal)
        #         #     state.append(origin)
        #         #     state.append(destiny)
        #         #     transition.append(state)
        #
        #         # DICTIONARY
        #         if not dic.has_key(origin):
        #             des = [[], []]
        #             dic[origin] = des
        #
        #         # Agregar./
        #
        #         continue
        #
        #     elif letter.isalpha():
        #         # print ("destino " + letter)
        #         # exists = False
        #         # for tran in transition:
        #         #     if tran[0] == signal and tran[1] == origin:
        #         #         tran[2].append(letter)
        #         #         exists = True
        #
        #         if signal == "0":
        #             temp = dic.get(origin)
        #             temp[0].append(letter)
        #             dic[origin] = temp
        #         else:
        #             temp = dic.get(origin)
        #             temp[1].append(letter)
        #             dic[origin] = temp
        #
        #         # if not exists:
        #         #     destiny.append(letter)
        #
        #     # print "ESTADO "
        #     # print state
        #
        # # transition = line.split(",")
        #
        # print "TRANS"
        # print transition
        # print "DICTO"
        # print dic
        global dic
        dic = lineToDictionary(line)

        # for state in transition:
        #     nueva0 = []
        #     nueva1 = []
        #     found0 = False
        #     found1 = False
        #     newState = state[2]
        #     for objective in state[2]:
        #
        #         for state in transition:
        #             if state[1] == objective:
        #                 if state[0] == "0":
        #                     if not found0:
        #                         nueva0.append(state[0])
        #                         nueva0.append(newState)
        #                         nueva0.append([])
        #                         found0 = True
        #
        #                     for element in state[2]:
        #                         nueva0[2].append(element)
        #
        #                 if state[0] == "1":
        #                     if not found1:
        #                         nueva1.append(state[0])
        #                         nueva1.append(newState)
        #                         nueva1.append([])
        #                         found1 = True
        #
        #                     for element in state[2]:
        #                         nueva1[2].append(element)
        #
        #     if found0:
        #         transition.append(nueva0)
        #     if found1:
        #         transition.append(nueva1)
        #
        #     print "TRANS"
        #     print transition
        findTransitions()


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
                        temp[0].append(i)

                    s1 = target[1]
                    for i in s1:
                        temp[1].append(i)

                dic[key] = temp
        #
        #     for element in transition:
        #         if element[1] == objective:
        #             if element[0] == "0":
        #                 if not found0:
        #                     nueva0.append(element[0])
        #                     nueva0.append(newState)
        #                     nueva0.append([])
        #                     found0 = True
        #
        #                 for element in element[2]:
        #                     nueva0[2].append(element)
        #
        #             if element[0] == "1":
        #                 if not found1:
        #                     nueva1.append(element[0])
        #                     nueva1.append(newState)
        #                     nueva1.append([])
        #                     found1 = True
        #
        #                 for element in element[2]:
        #                     nueva1[2].append(element)
        #
        # if found0:
        #     transition.append(nueva0)
        # if found1:
        #     transition.append(nueva1)
        #
        # print "TRANS"
        # print transition
        print dic


main()
