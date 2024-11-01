def ret_d (x,ppa):

    """
    Calcula el retorno promedio ya se por dias, meses o anual de un dataframe

    ppa = Periodo por 
    
    Calcula el retorno diario y elimina los valores NAN del dataframe,
    Luego calcula el retorno acumulado con el procuto de los retornos diarios.

    Posterior se calcula el retorno promedio diario  sumando 1 + el retorno acumulado elevando
    a 1 sobre el numero de periodos que tiene el dataframe
    por ultimo anualiza el retonodo promedio diario"""

    retorno = x.pct_change().dropna()
    retorno_acumulado = (1+ retorno).product()-1
    retorno_diario = (1 + retorno_acumulado)**(1/len(retorno))-1
    retorno_promedio_anual = ((1 + retorno_diario)**ppa)-1
    
    print(f"El retorno anualizado es: {retorno_promedio_anual}")

def rent1lin(frame,ppa):
    """esta función calcula la rentabilidad de stocks incluidos en un dataframe
    parámetro= frame que corresponde a un dataframe con rendimientos
            = ppa es el periódo en días
    """
    retorno=((frame+1).product()**(ppa/(len(frame)))-1)
    print(retorno)

def desvast (x, tiempo ="diario, mensual, anual"):

    """
    Calcula la volatilidad de un dataframe, dependiendo del tiempo, ya sea
    diario, mensual o anual
    
    Calcula el retorno diario y elimina los valores NAN del dataframe
    Luego calcula la volatilidad con la desviacion estandar de los retornos diarios

    Luego dependiendo del tiempo seleccionado
    este pasa por una serie de condiciones que va imprimiendo la volatilidad en el tiempo seleccionado
    """

    retornos = x.pct_change().dropna()

    volatilidad = retornos.std()

    if tiempo == "diario":

        print(f"La volatilidad diaria es: {volatilidad}")
    
    elif tiempo == "mensual":

        volatilidad_mensual = volatilidad * 22**(1/2)

        print(f"La volatilidad mensual para cada activo es: {volatilidad_mensual}")
    
    elif tiempo == "anual":

        volatilidad_anual = volatilidad * 252**(1/2)

        print(f"La volatilidad anualizada es: {volatilidad_anual}")
    else:

        print("Ingrese un tiempo valido, entre mensual, diario o anual")

    
def ret_acum (x):

    """
    Calcula el retorno acumulado de un dataframe
    
    Calcula el retorno diario y elimina los valores NAN del dataframe

    Luego calcula el retorno acumulado con el procuto de los retornos diarios"""

    retorno = x.pct_change().dropna()
    retorno_acumulado = (1+retorno).product()-1
    print(f"El retorno acumulado es: {retorno_acumulado}")


def rpm (x):

    """ Calcula el retorno diario o rendimiento promedio diaro de un dataframe"""

    retorno = x.pct_change().dropna()
    retorno_acumulado = (1+ retorno).product()-1
    retorno_diario = (1 + retorno_acumulado)**(1/len(retorno))-1

    print(f"El retorno promedio diario es: {retorno_diario}")


def percentile_1 (x):

    stock_ad = x['Adj Close']
    retorno = stock_ad.pct_change().dropna().sort_values()
    percentile_1 = np.percentile(retorno, 1)

    print(f"El {percentile_1} es: {percentile_1}")

    