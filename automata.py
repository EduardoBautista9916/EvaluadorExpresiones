from math import sqrt, pow
cont = 0
expresion = ""
num=""
var = ""
res = []
pilaNum = []
pilaOpe = []
pilaRes = []
pilaVar = []
errores = ["No puede terminar en un operador",""]

def inicio(cadena,cont,num,var):
    expresion=cadena
    if( expresion[cont] =="-" or expresion[cont] =="+"):
        signo(expresion,cont,num,var)
    elif(expresion[cont]=="#"):
        operador(expresion,cont,num,var)
    elif(cadena[cont].isalpha()):
        variable(expresion,cont,num,var)
    elif(expresion[cont].isnumeric()):
        numero(expresion,cont,num,var)
    elif(expresion[cont]=="("):
        parentesis(expresion,cont,num,var)
    else:
        error(expresion,cont)   

def numero(expresion,cont,num,var):
    print(expresion[cont],"es un numero")
    num += expresion[cont]
    cont += 1
    if(cont<len(expresion)):
        if(expresion[cont].isalpha()):
            pilaNum.append(num)
            pilaRes.append(num)
            res.append(num)
            num=""
            variable(expresion,cont,num,var)
        elif(expresion[cont].isnumeric() or expresion[cont]=="."):
            numero(expresion,cont,num,var)
        elif(isoperator(expresion[cont])):
            pilaNum.append(num)
            pilaRes.append(num)
            res.append(num)
            num=""
            operador(expresion,cont,num,var)
        elif(expresion[cont]=="("):
            pilaNum.append(num)
            pilaRes.append(num)
            res.append(num)
            num=""
            jerarquia("*")
            parentesis(expresion,cont,num,var)
        elif(expresion[cont]==")"):
            pilaNum.append(num)
            pilaRes.append(num)
            res.append(num)
            num=""
            parentesis(expresion,cont,num,var)
        else:
            error(expresion,cont)
    else:
        pilaNum.append(num)
        pilaRes.append(num)
        res.append(num)
        num=""
        vaciarPilaOpe()
        return

def variable(expresion,cont,num,var):
    print(expresion[cont],"es una variable")
    var += expresion[cont]
    pilaVar.append(var)
    pilaRes.append(var)
    res.append(var)
    var=""
    cont +=1
    if(cont<len(expresion)):
        if(expresion[cont].isalpha()):
            pilaOpe.append("*")
            variable(expresion,cont,num,var)
        elif(expresion[cont].isnumeric()):
            numero(expresion,cont,num,var)
        elif(isoperator(expresion[cont])):
            operador(expresion,cont,num,var)
        elif(expresion[cont]=="("):
            jerarquia("*")
            parentesis(expresion,cont,num,var)
        elif(expresion[cont]==")"):
            parentesis(expresion,cont,num,var)
        else:
            error(expresion,cont)
    else:
        vaciarPilaOpe()
        return

def operador(expresion,cont,num,var):
    print(expresion[cont],"es un operador")
    jerarquia(expresion[cont])
    cont +=1
    if(cont<len(expresion)):
        if(expresion[cont].isalpha()):
            variable(expresion,cont,num,var)
        elif(expresion[cont].isnumeric()):
            numero(expresion,cont,num,var)
        elif(expresion[cont]=="#"):
            operador(expresion,cont,num,var)
        elif(expresion[cont]=="("):
            parentesis(expresion,cont,num,var)
        else:
            error(expresion,cont)
    else:
        error(expresion,cont-1)

def signo(expresion,cont,num,var):
    print(expresion[cont],"es un signo")
    if(cont<len(expresion)):
        if(expresion[cont].isalpha()):
            var += expresion[cont]
            cont += 1
            variable(expresion,cont,num,var)
        elif(expresion[cont].isnumeric()):
            num += expresion[cont]
            cont +=1
            numero(expresion,cont,num,var)
        elif(expresion[cont]=="("):
            num+=expresion[cont]
            num+="1"
            pilaNum.append(num)
            num=""
            jerarquia("*")
            parentesis(expresion,cont,num,var)
        elif(expresion[cont]=="#"):
            num+=expresion[cont]
            num+="1"
            pilaNum.append(num)
            num=""
            jerarquia("*")
            parentesis(expresion,cont,num,var)
        else:
            error(expresion,cont)
    else:
        error(expresion,cont-1)

def parentesis(expresion,cont,num,var):
    if(expresion[cont]=="("):
        print(expresion[cont],"es un parentesis que abre")
        pilaOpe.append(expresion[cont])
        cont+=1
        if(cont<len(expresion)):
            if(expresion[cont].isalpha()):
                variable(expresion,cont,num,var)
            elif(expresion[cont].isnumeric()):
                numero(expresion,cont,num,var)
            elif(expresion[cont]=="#"):
                operador(expresion,cont,num,var)
            elif(expresion[cont]=="("):
                jerarquia("*")
                parentesis(expresion,cont,num,var)
            elif(expresion[cont]==")"):
                parentesis(expresion,cont,num,var)
            else:
                error(expresion,cont)
        else:
            error(expresion,cont)
    else:
        print(expresion[cont],"es un parentesis que cierra")
        vaciarParentesis()
        cont+=1
        if(cont<len(expresion)):
            if(expresion[cont].isalpha()):
                variable(expresion,cont,num,var)
            elif(expresion[cont].isnumeric()):
                numero(expresion,cont,num,var)
            elif(expresion[cont]=="#"):
                jerarquia("*")
                operador(expresion,cont,num,var)
            elif(expresion[cont]=="+" or expresion[cont]=="-" or expresion[cont]=="*" or expresion[cont]=="/" or expresion[cont]=="^"):
                operador(expresion,cont,num,var)
            elif(expresion[cont]=="("):
                jerarquia("*")
                parentesis(expresion,cont,num,var)
            elif(expresion[cont]==")"):
                parentesis(expresion,cont,num,var)
            else:
                error(expresion,cont)
        else:
            vaciarPilaOpe()
            return

def error(expresion,cont):
    print(expresion[cont],"Error")
    return

def isoperator(car):
    if(car=="+" or car=="-" or car=="*" or car=="/" or car=="#" or car=="^"):
        return True
    else:
        return False

def jerarquia(car):
    if(not len(pilaOpe)==0):
        if(car=="#" or car=="^"):
            print("Alto",pilaOpe[len(pilaOpe)-1])
            while((len(pilaOpe)!=0) and (pilaOpe[len(pilaOpe)-1]=="#" or pilaOpe[len(pilaOpe)-1]=="^")):
                pilaRes.append(pilaOpe.pop())
                evaluar(pilaRes[len(pilaRes)-1])
                print("entro ^ #")
        elif(car=="*" or car=="/"):
            print("Medio",pilaOpe[len(pilaOpe)-1])
            while((len(pilaOpe)!=0) and (pilaOpe[len(pilaOpe)-1]=="*" or pilaOpe[len(pilaOpe)-1]=="^" or pilaOpe[len(pilaOpe)-1]=="#" or pilaOpe[len(pilaOpe)-1]=="^")):
                pilaRes.append(pilaOpe.pop())
                evaluar(pilaRes[len(pilaRes)-1])
                print("entro * /")
        elif(car=="+" or car=="-"):
            print("Bajo",pilaOpe[len(pilaOpe)-1])
            while((len(pilaOpe)!=0) and (pilaOpe[len(pilaOpe)-1]=="+" or pilaOpe[len(pilaOpe)-1]=="-" or pilaOpe[len(pilaOpe)-1]=="*" or pilaOpe[len(pilaOpe)-1]=="^" or pilaOpe[len(pilaOpe)-1]=="#" or pilaOpe[len(pilaOpe)-1]=="^")):
                pilaRes.append(pilaOpe.pop())
                evaluar(pilaRes[len(pilaRes)-1])
                print("entro + -")
    pilaOpe.append(car)

def evaluar(ope):
    if ope == "#":
        a = float(res.pop())
        res.append(sqrt(a))
    elif ope == "^":
        a = float(res.pop())
        b = float(res.pop())
        res.append(pow(b,a))
    elif ope == "*":
        a = float(res.pop())
        b = float(res.pop())
        res.append(b*a)
    elif ope == "/":
        a = float(res.pop())
        b = float(res.pop())
        res.append(b/a)
    elif ope == "+":
        a = float(res.pop())
        b = float(res.pop())
        res.append(b+a)
    elif ope == "-":
        a = float(res.pop())
        b = float(res.pop())
        res.append(b-a)

def vaciarPilaOpe():
    while(len(pilaOpe)!=0):
        if(pilaOpe[len(pilaOpe)-1]=="("):
            print("error parentesis abre pero no cierra")
            break
        evaluar(pilaOpe[len(pilaOpe)-1])
        pilaRes.append(pilaOpe.pop())

def vaciarParentesis():
    while((len(pilaOpe)!=0) and (pilaOpe[len(pilaOpe)-1]!="(")):
        evaluar(pilaOpe[len(pilaOpe)-1])
        pilaRes.append(pilaOpe.pop())
    if(len(pilaOpe)!=0):
        pilaOpe.pop()

cadena = "5+(#(5^2+3-4)+"
inicio(cadena,cont,num,var)
print(pilaNum,pilaVar,pilaOpe,pilaRes)
print(res)