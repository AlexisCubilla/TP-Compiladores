import sys

arg = sys.argv[1]
# arg = "10 1510  0   1         66"
# arg = "5  1 3     88  2  1aa"
input = arg[0]
# input = arg[0]

count = 0



def match(entrada):
    global input, arg, count

    if (input == entrada):
        count = count + 1
        if(count < len(arg)):
            input = arg[count]
        else:
            input= "EOF"
    else:
        print(count, " count")
        raise Exception("Entrada no valida: " + input)


def lista():
        n = int(num())
        r = R()

        if (r):

            for i in range(0, len(r)):

                if (r[i] > n):
                    r.insert(i, n)
                    return r
            r.append(n)
            return r
        else:
            return [n]



def num():
    return (digito() + sec())

def digito():
    if (input == '0'):
        match('0')
        return ('0')
    elif (input == '1'):
        match('1')
        return ('1')
    elif (input == '2'):
        match('2')
        return ('2')
    elif (input == '3'):
        match('3')
        return ('3')
    elif (input == '4'):
        match('4')
        return ('4')
    elif (input == '5'):
        match('5')
        return ('5')
    elif (input == '6'):
        match('6')
        return ('6')
    elif (input == '7'):
        match('7')
        return ('7')
    elif (input == '8'):
        match('8')
        return ('8')
    else:
        match('9')
        return ('9')


def sec():
    if (input in '0123456789'):
        return num()
    else:
        return ' '


def R():
    if (input == ' '):
        sep()
        return lista()
    else:
        match("EOF")
        return []

def R2():
    if(input ==" "):
        sep()

def sep():
    match(" ")
    R2()

try:
    print(lista())
except Exception as error:
    print(error)