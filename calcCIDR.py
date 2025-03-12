# realiza o calculo de forma fragmentada
def binaryCalc(cidr):

    # lista fragmentada em 4 bytes
    listMask = [""] * 4 # 4 strings(bytes) vazios
    positionList : int = 0

    varLoop : int = 0
    while(varLoop < cidr):
        listMask[positionList] += "1"

        if len(listMask[positionList]) >= 8:
            positionList += 1

        varLoop += 1

    # loop teste de preenchimento de bit restante por '0'

    positionList = 0

    while(positionList < 4):
        if len(listMask[positionList]) < 8:
            bufferComplet = 8 - len(listMask[positionList]) # verifica quanto falta completar
            while(bufferComplet > 0):
                listMask[positionList] += "0"
                bufferComplet -= 1

        positionList += 1

    return listMask


# Para realizar o calculo binário para decimal
def binaryToDecimal(binaryNumStr):
 
    if type(binaryNumStr) == list:
        
        position : int = 0
        loopVarTotal : int = 0

        binaryNumInt : int = [0] * 4

        while(loopVarTotal < (len(binaryNumStr) * 8)):
            loopVarOct : int = 7
            while (loopVarOct >= 0):
            
                if binaryNumStr[position][loopVarOct] == "1":
                    binaryNumInt[position] += 2 ** (7 - loopVarOct)

                loopVarTotal +=1
                loopVarOct -= 1
            
            position += 1

        return binaryNumInt

# Transforma o CIDR em uma mascara de rede
def cidrToMask(cidr : int):
    binaryList = binaryCalc(cidr)
    decimalList = binaryToDecimal(binaryList)

    netMask = ".".join(map(str,decimalList))

    return netMask