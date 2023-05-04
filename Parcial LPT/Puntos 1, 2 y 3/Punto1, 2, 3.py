def mostrar(diccionario: dict):
    for clave, valor in diccionario.items():
        print(clave+':',valor)

def eliminar_recursion(gramatica: dict) -> dict:
    new_gramatica = {}
    for no_terminal, producciones in gramatica.items():
        alpha = []
        betha = []
        new_no_terminal = no_terminal + '\''
        for cadena in producciones:
            if 'λ' in cadena:
                break
            copia = cadena[:] 
            if copia[0] == no_terminal:
                copia.remove(copia[0])
                copia.append(new_no_terminal)
                alpha.append(copia)
            else:
                copia.append(new_no_terminal)
                betha.append(copia)
        if len(alpha) > 0: 
            new_gramatica[no_terminal] = betha
            new_gramatica[new_no_terminal] = alpha
            lam = ['λ']
            new_gramatica[new_no_terminal].append(lam)
        else:
            new_gramatica[no_terminal] = producciones

    return new_gramatica

# Verificar si es terminal o no terminal
def terminal(gramatica,caracter) -> bool:
    if caracter in gramatica.keys():
        return False
    else:
        return True

def primeros_algorithm(n,gramatica: dict, producciones, no_terminal, primeros: dict) -> dict:
    primeros[no_terminal] = set()  # Usamos un conjunto para evitar duplicados

    for cadena in producciones:
        if 'λ' in cadena:
            primeros[no_terminal].add('λ')
        elif terminal(gramatica, cadena[0]):
            primeros[no_terminal].add(cadena[0])
        else:
            # Calculamos el conjunto de primeros del primer símbolo no-terminal de la cadena
            primeros_siguiente = primeros_algorithm(0,gramatica, gramatica[cadena[0]], cadena[0], primeros)
            primeros[no_terminal].update(primeros_siguiente)  # Agregamos los primeros de la cadena

            # Si la cadena puede derivar en λ, calculamos los primeros de la siguiente cadena recursivamente
            while 'λ' in primeros_siguiente and n+1 < len(cadena):
                n= n+1
                primeros_siguiente.remove('λ')  # No queremos incluir λ en los primeros de la siguiente cadena
                if terminal(gramatica,cadena[n]):
                    primeros_siguiente.add(cadena[n])
                else:
                    primeros_siguiente.update(primeros_algorithm(n,gramatica, gramatica[cadena[n]], cadena[n], primeros))
                primeros[no_terminal].update(primeros_siguiente)
            if 'λ' in primeros[no_terminal]:
                primeros[no_terminal].remove('λ')
    return primeros[no_terminal]
    #mostrar(primeros)

def sacar_primeros(new_gramatica):
    primero = {}
    for no_terminal, producciones in new_gramatica.items():
        primeros = {}
        n = 0
        conjunto = primeros_algorithm(n,new_gramatica,producciones,no_terminal,primeros)
        primero[no_terminal] = conjunto
    return primero

def siguientes_algorithm(i,no_terminal,gramatica,primeros,siguientes,inicial):
    
    if no_terminal not in siguientes:
        siguientes[no_terminal] = set()
        if inicial == no_terminal:
            siguientes[no_terminal].add('$') 
    for nos_terminal in gramatica.keys():
        for producciones in gramatica[nos_terminal]:
            n = 0
            for caracter in producciones:
                n = n+1
                if caracter == no_terminal:
                    betha = producciones[n:]
                    if len(betha) > 0:
                        if betha[0] == 'λ':
                            if nos_terminal in siguientes.keys():
                                siguientes[no_terminal].update(siguientes[nos_terminal])
                            else:
                                siguientes[no_terminal].update(siguientes_algorithm(i,nos_terminal,gramatica,primeros,siguientes,inicial))
                        elif terminal(gramatica,betha[0]):
                            siguientes[no_terminal].add(betha[0])
                        else:
                            if 'λ' in primeros[betha[0]]:
                                siguientes[no_terminal].update(siguientes_algorithm(i,nos_terminal,gramatica,primeros,siguientes,inicial))
                            siguientes[no_terminal].update(primeros[betha[0]])
                    else:
                        if nos_terminal in siguientes.keys():
                            siguientes[no_terminal].update(siguientes[nos_terminal])
                        else:
                            siguientes[no_terminal].update(siguientes_algorithm(i,nos_terminal,gramatica,primeros,siguientes,inicial))
    if 'λ' in siguientes[no_terminal]:
        siguientes[no_terminal].remove('λ')
    return siguientes[no_terminal]

def sacar_siguientes(new_gramatica,primeros):
    i = 0
    siguiente = {}
    
    for no_terminal in new_gramatica.keys():
        siguientes = {}
        n = 0
        if i == 0:
            inicial = no_terminal
            i = 1
        conjunto = siguientes_algorithm(i,no_terminal,new_gramatica,primeros,siguientes,inicial)
        siguiente[no_terminal] = conjunto
    return siguiente

def sacar_pred(new_gramatica,siguientes):
    pred = {}
    primeros = {}
    for no_terminal in new_gramatica.keys():
        n = 0
        for cadena in new_gramatica[no_terminal]:
            n = n+1
            #regla = no_terminal +' -> ' + str(cadena)
            regla = no_terminal + str(n)
            pred[regla] = set()
            if 'λ' in cadena:
                pred[regla].update(siguientes[no_terminal])
            elif terminal(new_gramatica, cadena[0]):
                pred[regla].add(cadena[0])
            elif cadena[0] in new_gramatica.keys():
                pred[regla].update(primeros_algorithm(0,new_gramatica,cadena,no_terminal,primeros))
    return pred

def ver_factor_comun(gramatica):

    for no_terminal, producciones in gramatica.items():
        n = len(producciones)
        if n > 0:
            min = len(producciones[0])
            for produccion in gramatica[no_terminal]:
                if len(produccion) < min:
                    min = len(produccion)
            if n > 1:
                for i in range(0,n):
                    for j in range(0,n):
                        factor1 = ''
                        factor2 = ''
                        if i != j:
                            for k in range(0,min):
                                factor1 = factor1 + str(gramatica[no_terminal][i][k])
                                factor2 = factor2 + str(gramatica[no_terminal][j][k])
                                if factor1 == factor2:
                                    return 1
    return 0

def ver_factor_comun(gramatica):

    for no_terminal, producciones in gramatica.items():
        n = len(producciones)
        if n > 0:
            min = len(producciones[0])
            for produccion in gramatica[no_terminal]:
                if len(produccion) < min:
                    min = len(produccion)
            if n > 1:
                for i in range(0,n):
                    for j in range(0,n):
                        factor1 = ''
                        factor2 = ''
                        if i != j:
                            for k in range(0,min):
                                factor1 = factor1 + str(gramatica[no_terminal][i][k])
                                factor2 = factor2 + str(gramatica[no_terminal][j][k])
                                if factor1 == factor2:
                                    return True
    return False

def ver_iguales_pred(gramatica,pred):
    for no_terminal in gramatica.keys():
        conjuntos = []
        interseccion = {}
        n = 1
        for produccion in gramatica[no_terminal]:
            nombre_set_pred = str(no_terminal) + str(n)
            conjuntos.append(pred[nombre_set_pred])
            n = n+1 
        interseccion = set.intersection(*conjuntos)
        n = n+1
        if len(interseccion) > 0:
            return True
    return False

def verificar_ll1(gramatica,pred):
    if ver_factor_comun(gramatica):
        print('La gramatica no es LL(1) porque tiene factores comunes\n')
    if ver_iguales_pred(gramatica,pred):
        print('La gramatica no es LL(1) porque en el conjunto de predicciones hay elementos iguales\n')
    if not(ver_factor_comun(gramatica)) and not(ver_iguales_pred(gramatica,pred)):
        print('La gramatica es LL(1)')

def resultados(gramatica, recursion, ejercicio):
    print('\nEjercicio: '+str(ejercicio))
    print('gramatica inicial: \n')
    mostrar(gramatica)
    new_gramatica = {}
    if recursion == 1:
        print('\ngramatica sin recursion por la izquierda:\n')
        new_gramatica = eliminar_recursion(gramatica)
        mostrar(new_gramatica)
    else: 
        new_gramatica = gramatica
    print('\nPrimeros:\n')
    primeros =sacar_primeros(new_gramatica) 
    mostrar(primeros)
    print('\nSiguientes:\n')
    siguientes = sacar_siguientes(new_gramatica,primeros)
    mostrar(siguientes)
    print('\nPredicciones:\n')
    pred = sacar_pred(new_gramatica,siguientes)
    mostrar(pred)
    print('\nVerificacion LL(1)\n')
    verificar_ll1(new_gramatica,pred)

#Prueba de los algoritmos
'''
gramatica = {'C':[['otra'],['λ']],'A': [['A','otro'],['algo','B'],['A','nose'],['λ']], 'B':[['C','S','A','algo'],['nose','xD']],
             'S':[['talvez'],['wow']]}
      
# Ejemplo diapositiva
gramatica = {'A':[['B','C'],['ant','A','all']],
             'B':[['big','C'],['bus','A','boss'],['λ']],
             'C':[['cat'],['cow']]}
'''

# Ejercicio 1 parcial
gramatica = {'S':[['A','B','C'],['D','C']],
             'A':[['dos','B','tres'],['λ']],
             'B':[['B','cuatro','C','cinco'],['λ']],
             'C':[['seis','A','B'],['λ']],
             'D':[['uno','A','E'],['B']],
             'E':[['tres']]}
resultados(gramatica,1,1)  

# Ejercicio 2 parcial
gramatica = {'S':[['B','A','uno'],['dos','C'],['λ']],
             'A':[['tres','B','C'],['cuatro'],['λ']],
             'B':[['A','cinco','C','seis'],['λ']],
             'C':[['siete','B'],['λ']]}
resultados(gramatica,0,2)
# Ejercicio 3 parcial
gramatica = {'S':[['A','B','C'],['S','uno']],
             'A':[['dos','B','C'],['λ']],
             'B':[['C','tres'],['λ']],
             'C':[['cuatro','B'],['λ']]}
resultados(gramatica,1,3)
