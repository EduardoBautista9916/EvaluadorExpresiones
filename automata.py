from math import sqrt, pow
import time
cont = 0
expresion = ""
num=""
var = ""
res = []
pilaNum = []
pilaOpe = []
pilaRes = []
pilaVar = []
errores = ["No puede terminar en un operador","Caracter no valido", "No puede terminar en un signo" ,"Parentesis que abre pero no cierra", "Parentesis que cierra pero no abre", "No puede iniciar con este caracter", "No se Puede abrir y cerrar un parentesis"]

def inicio(cadena,cont,num,var, ui):
    expresion=cadena
    if( expresion[cont] =="-" or expresion[cont] =="+"):
        signo(expresion,cont,num,var,ui)
    elif(expresion[cont]=="#"):
        operador(expresion,cont,num,var,ui)
    elif(cadena[cont].isalpha()):
        variable(expresion,cont,num,var,ui)
    elif(expresion[cont].isnumeric()):
        numero(expresion,cont,num,var,ui)
    elif(expresion[cont]=="("):
        parentesis(expresion,cont,num,var,ui)
    else:
        if(isoperator(expresion[cont]) or expresion[cont]==")"):
            error(expresion,cont,5,ui)
        else:
            error(expresion,cont,1,ui)   

def numero(expresion,cont,num,var,ui):
    print(expresion[cont]," es un numero")
    ui.txtCalculate.setText(expresion[cont])
    ui.imprimirProscess(expresion[cont]+" es un Numero")
    ui.pbCaculate.setValue(100)
    time.sleep(0.5)
    num += expresion[cont]
    cont += 1
    if(cont<len(expresion)):
        if(expresion[cont].isalpha()):
            pilaNum.append(num)
            pilaRes.append(num)
            res.append(num)
            num=""
            variable(expresion,cont,num,var,ui)
        elif(expresion[cont].isnumeric() or expresion[cont]=="."):
            numero(expresion,cont,num,var,ui)
        elif(isoperator(expresion[cont])):
            pilaNum.append(num)
            pilaRes.append(num)
            res.append(num)
            num=""
            operador(expresion,cont,num,var,ui)
        elif(expresion[cont]=="("):
            pilaNum.append(num)
            pilaRes.append(num)
            res.append(num)
            num=""
            jerarquia("*")
            parentesis(expresion,cont,num,var,ui)
        elif(expresion[cont]==")"):
            pilaNum.append(num)
            pilaRes.append(num)
            res.append(num)
            num=""
            parentesis(expresion,cont,num,var,ui)
        else:
            error(expresion,cont,1,ui)
    else:
        pilaNum.append(num)
        pilaRes.append(num)
        res.append(num)
        num=""
        vaciarPilaOpe(ui)
        ui.txtResult.setText(str(res[0]))
        res.clear()
        imprimirNotPos(ui)
        return

def variable(expresion,cont,num,var,ui):
    print(expresion[cont],"es una variable")
    ui.txtCalculate.setText(expresion[cont])
    ui.imprimirProscess(expresion[cont]+" es una Variable")
    time.sleep(0.5)
    var += expresion[cont]
    pilaVar.append(var)
    pilaRes.append(var)
    res.append(var)
    var=""
    cont +=1
    if(cont<len(expresion)):
        if(expresion[cont].isalpha()):
            pilaOpe.append("*")
            variable(expresion,cont,num,var,ui)
        elif(expresion[cont].isnumeric()):
            numero(expresion,cont,num,var,ui)
        elif(isoperator(expresion[cont])):
            operador(expresion,cont,num,var,ui)
        elif(expresion[cont]=="("):
            jerarquia("*")
            parentesis(expresion,cont,num,var,ui)
        elif(expresion[cont]==")"):
            parentesis(expresion,cont,num,var,ui)
        else:
            error(expresion,cont,1,ui)
    else:
        vaciarPilaOpe(ui)
        ui.txtResult.setText(str(res[0]))
        res.clear()
        imprimirNotPos(ui)
        return

def operador(expresion,cont,num,var,ui):
    print(expresion[cont],"es un operador")
    ui.txtCalculate.setText(expresion[cont])
    ui.imprimirProscess(expresion[cont]+" es un Operador")
    time.sleep(0.5)
    jerarquia(expresion[cont])
    cont +=1
    if(cont<len(expresion)):
        if(expresion[cont].isalpha()):
            variable(expresion,cont,num,var,ui)
        elif(expresion[cont].isnumeric()):
            numero(expresion,cont,num,var,ui)
        elif(expresion[cont]=="#"):
            operador(expresion,cont,num,var,ui)
        elif(expresion[cont]=="("):
            parentesis(expresion,cont,num,var,ui)
        else:
            error(expresion,cont,1,ui)
    else:
        error(expresion,cont-1,0,ui)

def signo(expresion,cont,num,var,ui):
    print(expresion[cont],"es un signo")
    ui.txtCalculate.setText(expresion[cont])
    ui.imprimirProscess(expresion[cont]+" es un Signo")
    time.sleep(0.5)
    if(cont<len(expresion)):
        if(expresion[cont].isalpha()):
            var += expresion[cont]
            cont += 1
            variable(expresion,cont,num,var,ui)
        elif(expresion[cont].isnumeric()):
            num += expresion[cont]
            cont +=1
            numero(expresion,cont,num,var,ui)
        elif(expresion[cont]=="("):
            num+=expresion[cont]
            num+="1"
            pilaNum.append(num)
            num=""
            jerarquia("*")
            parentesis(expresion,cont,num,var,ui)
        elif(expresion[cont]=="#"):
            num+=expresion[cont]
            num+="1"
            pilaNum.append(num)
            num=""
            jerarquia("*")
            parentesis(expresion,cont,num,var,ui)
        else:
            error(expresion,cont,1,ui)
    else:
        error(expresion,cont-1,2,ui)

def parentesis(expresion,cont,num,var,ui):
    if(expresion[cont]=="("):
        print(expresion[cont],"es un parentesis que abre")
        ui.txtCalculate.setText(expresion[cont])
        ui.imprimirProscess(expresion[cont]+" es un Parentesis que Abre")
        time.sleep(0.5)
        pilaOpe.append(expresion[cont])
        cont+=1
        if(cont<len(expresion)):
            if(expresion[cont].isalpha()):
                variable(expresion,cont,num,var,ui)
            elif(expresion[cont].isnumeric()):
                numero(expresion,cont,num,var,ui)
            elif(expresion[cont]=="#"):
                operador(expresion,cont,num,var,ui)
            elif(expresion[cont]=="("):
                jerarquia("*")
                parentesis(expresion,cont,num,var,ui)
            elif(expresion[cont]==")"):
                error(expresion,cont,6,ui)
            else:
                error(expresion,cont,1,ui)
        else:
            error(expresion,cont-1,3,ui)
    else:
        print(expresion[cont],"es un parentesis que cierra")
        ui.txtCalculate.setText(expresion[cont])
        ui.imprimirProscess(expresion[cont]+" es un Parentesis que Cierra")
        vaciarParentesis(ui)
        cont+=1
        if(cont<len(expresion)):
            if(expresion[cont].isalpha()):
                variable(expresion,cont,num,var,ui)
            elif(expresion[cont].isnumeric()):
                numero(expresion,cont,num,var,ui)
            elif(expresion[cont]=="#"):
                jerarquia("*")
                operador(expresion,cont,num,var,ui)
            elif(expresion[cont]=="+" or expresion[cont]=="-" or expresion[cont]=="*" or expresion[cont]=="/" or expresion[cont]=="^"):
                operador(expresion,cont,num,var,ui)
            elif(expresion[cont]=="("):
                jerarquia("*")
                parentesis(expresion,cont,num,var,ui)
            elif(expresion[cont]==")"):
                parentesis(expresion,cont,num,var,ui)
            else:
                error(expresion,cont,1,ui)
        else:
            ui.txtResult.setText(str(res[0]))
            res.clear()
            vaciarPilaOpe(ui)
            imprimirNotPos(ui)
            return

def error(expresion,cont,nMen,ui):
    print(expresion[cont],errores[nMen])
    ui.imprimirError(expresion[cont]+" "+errores[nMen])
    time.sleep(0.5)
    pilaNum.clear()
    pilaVar.clear()
    pilaRes.clear()
    pilaOpe.clear()
    res.clear()
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

def imprimirNotPos(ui):
    for i in pilaRes:
        cad = ui.txtPostfix.text()
        ui.txtPostfix.setText(cad+" "+i)
    pilaRes.clear()
    pilaNum.clear()
    pilaOpe.clear()
    pilaVar.clear()

def vaciarPilaOpe(ui):
    while(len(pilaOpe)!=0):
        if(pilaOpe[len(pilaOpe)-1]=="("):
            print("error parentesis abre pero no cierra")
            ui.imprimirError(errores[3])
            break
        print(res)
        evaluar(pilaOpe[len(pilaOpe)-1])
        pilaRes.append(pilaOpe.pop())

def vaciarParentesis(ui):
    while(len(pilaOpe)!=0 and pilaOpe[len(pilaOpe)-1]!="("):
        print(res)
        evaluar(pilaOpe[len(pilaOpe)-1])
        pilaRes.append(pilaOpe.pop())
    if(len(pilaOpe)!=0):
        pilaOpe.pop()