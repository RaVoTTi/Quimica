VOLTAJE = {
'Li(+1)/Li°':   -3.05,       
'Cs(+1)/Cs°':   -3.02,           
'Rb(+1)/Rb°':   -2.99,           
'K(+1)/K°':    -2.93,           
'Ba(+2)/Ba2°': -2.90,        
'Sr(+2)/Sr°':   -2.89,        
'Ca(+2)/Ca°':   -2.87,        
'Na(+1)/Na°':   -2.71,          
'Mg(+2)/Mg°':   -2.37,        
'Be(+2)/Be°':   -1.85,        
'Al(+3)/Al°':   -1.66,        
'Mn(+2)/Mn°':   -1.18,
'Sn(+4)/Sn°':   -1.07,        
'2H2O/H2°,2OH(-1)':-0.83,        
'Zn(+2)/Zn°':   -0.76,        
'Cr(+3)/Cr°':  -0.74,           
'Fe(+2)/Fe°':   -0.44,        
'Cd(+2)/Cd°':    -0.40,                                             
'PbSO4/Pb°,SO4(-2)':-0.31,                   
'Co(+2)/Co°':   -0.28,        
'Ni(+2)/Ni°':    -0.25,         
'Sn(+2)/Sn°':-0.14,         
'Рb(+2)/Pb°':-0.13,
'Fe(+3)/Fe°':-0.04,                                         
'2H(+1)/H2°':   0.00,
'Sn(+4)/Sn(+2)':+0.13 ,          
'Cu(+2)/Cu(+1)':+0.15 ,                                 
'SO4(-2),4H/SO2,2H20':+0.20 ,          
'AgCl/Ag°,Cl(-1)':+0.22 ,                                 
'Cu(+2)/Cu°':+0.34 ,
'O2°,2H2O/4OH(-1)':+0.40 ,                                                                   
'I2°/2I(-1)':+0.53 ,                                    
'MnO4(-1),2H20/MnO2,4OH(-1)':+0.59 ,
'O2°,2H(+1)/H202':+0.68 ,
'Fe(3+)/Fe(+2)':+0.77 ,                                    
'Ag(+1)/Ag°':+0.80 ,                                    
'Hg2(+2)/2Hg°':+0.85 ,                                   
'Hg(+2)/Hg°':+0.92 ,
'NO3(-1),4H(+1)/NO2,2H20    ':+0.96 ,           
'Br2°/2Br(-1)':+1.07 ,                                    
'O2°,4H(+1)/2H20':+1.23 ,
'MnO2(-1),4H(+1)/Mn(+2),2H2O ':+1.23 ,                                                                
'Cr2O7(-1),14H(+1)/2Cr(+3),7H2O':+1.33 ,
'Cl2°/Cl(-1)':+1.36 ,                                 
'Au(+3)/Au°':+1.50 ,                                                                   
'MnO4(-1),8H(+1)/Mn(+2),4H20':+1.51 ,
'Ce(+4)/Ce(+3)':+1.61 ,   
'PbO2,2H(+1),SO4(-2)/PbSO4,':+1.70 , 
'2H202,2H(+1)/2H20':+1.77 ,                                  
'Co(+3)/Co(+2)':+1.82 ,                                
'O3°,2H(+1)/O2°,H20':+2.07 , 
'F2°/2F(-1)':+2.87 ,                                  
} 

# Funcion para buscar carga
def search_q(lista):
    try:
        numMin = lista.index('(') + 1
        numMax = lista.index(')')
        return lista[numMin:numMax]
    except:
        try:
            lista.index('°')
            return 0
        except:
            print('Ingresa bien las cargas')
# Busca el voltaje de esa reaccion
def opuesto(numero):
    if numero >= 0:
        return -(numero)
    else:
        return abs(numero)


# A = delta diferencia
def A_q(q1, q2):            
    tot = (q1 - q2)
    if tot < 0:
        tot = -(tot)
    return tot

# Funcion para desglosar la formula
def desglosar(lista):
    anodo = list()
    catodo = list()
    lista = lista.split('//')

    anodo = lista[0].split('/')
    catodo = lista[1].split('/')
    
    return anodo , catodo
# rota la reaccion para verificar en caso de que sea una reaccion de oxidacion
def rotar(lista):
    temp = list()
    lista = lista.split('/')
    numWord = int(len(lista) - 1)
    for word in range(len(lista)):
        temp.append(lista[numWord - word])
    result = temp[0] + '/' + temp[1]
    return result

        
# Funcion para buscar indice
def search_indice(lista):
    indice = None
    rango = len(lista)
    for i in range(rango):
        temp = lista[i]
        try:
            if type(int(temp)) is int:  
                if indice is None:
                    indice = temp         
                else:    
                    indice = indice + temp
        except:    
            if indice is None:
                return 1
            else:
                break
    return int(indice)

# cambia el indice del resultado
def change_indice(indice, lista, k):
    indice = int(indice)
    try:
        if int(lista[0]) == indice:
            result = str(indice * k) + str(lista[1:-1])
    except:
        if k != 1:
            result = str(k) + lista  
        else:
            result = lista              
    return str(result)

# Funcion Simplificar
def simplificar(A_qAnodo, A_qCatodo):
    if (A_qAnodo % 2 +  A_qCatodo % 2) == 0:
        return (A_qAnodo / 2),(A_qCatodo / 2) 
    elif (A_qAnodo % 2 +  A_qCatodo % 2) == 0:
        return (A_qAnodo / 3),(A_qCatodo / 3)
    else:
        return int(A_qAnodo), int(A_qCatodo)

if __name__ == "__main__":
    flag = 1
    while flag == 1:
        ANODO = []
        CATODO = []

        indexAnodo = []
        indexCatodo = []

        chargeAnodo = []
        chargeCatodo = []

        resultAnodo = []
        resultCatodo = []

        voltajeAnodo = None
        voltajeCatodo = None
        voltajeResult = None 

        formulaCelda = str(input('Ingrese la reaccion de la celda galvanica: '))
        if formulaCelda == 'info':
            for items in VOLTAJE:
                
                print('----> {} '.format(items))
        else:
            try:
                formulaCeldaProcesada = formulaCelda.split('//')
                ANODO , CATODO = desglosar(formulaCelda)
            except:
                print('#### Ingrese la reaccion con el formato correcto ####'.center(50).upper())
                continue
        
        
        for i in range(len(CATODO)):
            indexCatodo.append(int(search_indice(CATODO[i])))
            chargeCatodo.append( int(search_q(CATODO[i])))
        for i in range(len(ANODO)):
            indexAnodo.append(int(search_indice(ANODO[i])))
            chargeAnodo.append( int(search_q(ANODO[i])))
        
        # A diferencia de cargas
        A_qCatodo = int(A_q(chargeCatodo[0], chargeCatodo[1]))
        A_qAnodo  = int(A_q(chargeAnodo[0], chargeAnodo[1]))

        A_qAB, A_qCD = simplificar(A_qAnodo,A_qCatodo)
        A_qAB = int(A_qAB)
        A_qCD = int(A_qCD)
        # Voltaje
        try:
            voltajeAnodo = VOLTAJE.get(formulaCeldaProcesada[0], None)
            voltajeCatodo = VOLTAJE.get(formulaCeldaProcesada[1], None)
            if voltajeAnodo is None:
                temp = str(rotar(formulaCeldaProcesada[0]))
                voltajeAnodo = VOLTAJE.get(temp, None)
                if voltajeAnodo is None:
                    print('Voltaje Anodo no encontrado')
            voltajeAnodo = opuesto(voltajeAnodo)
            
            if voltajeCatodo is None:
                temp = str(rotar(formulaCeldaProcesada[1]))
                voltajeCatodo = VOLTAJE.get(temp, None)

                if voltajeCatodo is None:
                    print('Voltaje Catodo no encontrado')

            voltajeResult = voltajeCatodo + voltajeAnodo
        except:
            print('La reaccion del catodo no esta disponible o esta mal escrita')
            voltajeCatodo = 'X'
            voltajeAnodo = 'X'
            voltajeResult = voltajeCatodo + voltajeAnodo
  
            

        for i in range(len(CATODO)):
            resultCatodo.append(change_indice(indexCatodo[i],CATODO[i], A_qAB))
        for i in range(len(ANODO)):
            resultAnodo.append( change_indice(indexAnodo[i],ANODO[i], A_qCD))

        print(formulaCelda)
        if chargeAnodo[0] < chargeAnodo[1]:        
            print('(  {}    ====> {} + {}e- ) {} Anodo se oxida // V = {}'.format(ANODO[0], ANODO[1], A_qAnodo, A_qCD, voltajeAnodo))
        else:
            print('(  {} + {}e-   ====> {}  ) {} Anodo se oxida // V = {}'.format(ANODO[0], A_qAnodo,ANODO[1], A_qCD, voltajeAnodo))
        if chargeCatodo[0] > chargeCatodo[1]:        
            print('({} + {}e- ====>  {}) {} Catodo se reduce// V = {}'.format(CATODO[0],A_qCatodo,CATODO[1], A_qAB, voltajeCatodo))
        else:
            print('(  {}  ====> {}e- + {}  ) {} Catodo se reduce // V = {}'.format(CATODO[0], A_qCatodo,CATODO[1], A_qCD, voltajeCatodo))
        print('_____________________________')
        print('{} + {} + {}e- ====> {} + {} + {}e- // Vt = {}'.format(resultCatodo[0],resultAnodo[0], A_qCatodo ,resultCatodo[1],resultAnodo[1], A_qAnodo, voltajeResult))
        
        print('Valentin NO COPYRIGHT')
        flag = int(input('Quiere continuar: '))


           
          
     
       