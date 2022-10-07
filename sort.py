import sys

arg = sys.argv[1]

# print(len(arg))

input = arg[0]

count = 0


def match(entrada):

    global input, arg, count

    # print(entrada)

    if (input == entrada):

        if(count+1 < len(arg)):

            while (count+1 < len(arg)):

                count = count+1
            
                input = arg[count]

                if (not (entrada == ' ' and input == ' ')):
        
                    break
        else:
            # print(entrada)
            input='EOF'

    else:
        # print(entrada,input)
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

   
    return digito()+sec()


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
        # print(input)
        match('9')
        return ('9')


def sec():
    if (input in '0123456789'):
        # print(input)
        return num()
    else:
  
        return ' '


def R():

    if (input == ' '):
        match(' ')
        return lista()
    else:
        match('EOF')
        return []


try:
    print(lista())
except Exception as error:
    print(error)
