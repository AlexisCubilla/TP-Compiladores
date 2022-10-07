import sys

arg = sys.argv[1]

input = arg[0]

count = 0

def match(entrada):

    global input, arg, count
 
    if(input == entrada):

        if(count < len(arg)):

            while(True):
                
                count=count+1

                input=arg[count]

                print(input)

                if(not(entrada == '' and input =='')):
                    break
    else:
        print(count)
        raise Exception("Entrada no valida:" + entrada+ ' == ' + input )
                
def lista ():

    n= num()
    match('')    
    r= R()       

    if(r):                            

        for i in range(0,len(r)):

            if( r[i] > n ):
                r.insert(i,n)
                return r
        r.append(n)  
        return r
    else:
        return [n]

def num ():

    return int(digito()+sec())

def digito ():

    if(input=='0'):
        match('0')
        return('0')
    elif(input=='1'):
        match('1')
        return('1')
    elif(input=='2'):
        match('2')
        return('2')
    elif(input=='3'):
        match('3')
        return('3')
    elif(input=='4'):
        match('4')
        return('4')
    elif(input=='5'):
        match('5')
        return('5')
    elif(input=='6'):
        match('6')
        return('6')
    elif(input=='7'):
        match('7')
        return('7')
    elif(input=='8'):
        match('8')
        return('8')
    else:
        match('9')
        return('9')

def sec():
    if(input != ''):
        match('')
        return num()
    else:
        return ''

def R():
    global input,arg,count
    if(count < len(arg)):
        return lista()
    else:
        return []

try:
    lista()
except Exception as error:
    print(error)

        