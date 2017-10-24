
def main():
    NAME = "input.txt"
    ALPHABET = {"0", "1"}

    # fileName = raw_input("Ingrese el nombre del archivo:")
    file = open(NAME, 'r')

    for line in file:
        print line
        transition = []
        destiny = []
        state = []
        flag = True
        signal = -1
        origin = ""
        for letter in line:
            if letter in ALPHABET:
                # state.append(destiny)
                # transition.append(state)

                # RESET
                flag = True
                state = []
                destiny = []
                # RESET./

                # state.append(letter)
                signal = letter
                # print ("signo " + letter)
                continue

            elif (flag and letter.isalpha()):
                flag = False
                # state.append(letter)
                origin = letter
                # print ("origen " + letter)

                # Agregar
                exists = False
                for tran in transition:
                    if tran[0] == signal and tran[1] == origin:
                        exists = True

                if not exists:
                    state.append(signal)
                    state.append(origin)
                    state.append(destiny)
                    transition.append(state)
                # Agregar./

                continue

            elif letter.isalpha():
                # print ("destino " + letter)
                exists = False
                for tran in transition:
                    if tran[0] == signal and tran[1] == origin:
                        tran[2].append(letter)
                        exists = True

                if not exists:
                    destiny.append(letter)

            # print "ESTADO "
            # print state



        # transition = line.split(",")

        print "TRANS"
        print transition

def guille():
    nfa = ""
    archivo = open("input.txt","r")
    for linea in archivo:
        nfa += linea

    nfa = nfa.split(")")
    print nfa
    transiciones = []
    transiciones_diccionario = {}
    for i in range(len(nfa)):
        estado = ""
        if(i == 0):
            for j in range(len(nfa[i])):
               if(nfa[i][j] != '{' and nfa[i][j] != '('  and nfa[i][j] != ')' and nfa[i][j] != '}'):
                   estado += nfa[i][j]
        else:
            for j in range(1,len(nfa[i])):
                if (nfa[i][j] != '{' and nfa[i][j] != '(' and nfa[i][j] != ')' and nfa[i][j] != '}'):
                    estado += nfa[i][j]
        transiciones.append(estado)

    for i in range(len(transiciones)):
        print transiciones[i]

    print transiciones

main()