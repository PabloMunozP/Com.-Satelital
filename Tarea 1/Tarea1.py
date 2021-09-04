import math

def seno(grados):# para aceptar grados y retornar el seno
    return math.sin(math.radians(grados))

def coseno(grados):# para aceptar grados y retornar el coseno
    return math.cos(math.radians(grados))

def arccos(grados):
    return math.degrees(math.acos(math.radians(grados)))

def arcseno(grados):
    return math.degrees(math.asin(math.radians(grados)))

def arctan(grados):
    return math.degrees(math.atan(math.radians(grados)))

def angulo_gamma(Lt,lt,Ls,ls):
    #Lt: Latitud terrena // Ls: Latitud satelite
    #lt: longitud terrena // ls: longitud satelite
    result=coseno(Lt)*coseno(Ls)*coseno(ls-lt) + seno(Lt)*seno(Ls)
    return arccos(result)

def angulo_elevacion(gamma,radioSatelite,radioTierra):

    result= seno(gamma)/math.pow((1+math.pow((radioTierra/radioSatelite),2) - 2*(radioTierra/radioSatelite)*coseno(gamma) ), 0.5)
    return arccos(result)

def angulo_alfa(Lt,lt,ls):
    #Lt: Latitud terrena // Ls: Latitud satelite
    #lt: longitud terrena // ls: longitud satelite
    result= (math.tan(math.radians(abs(ls-lt)))) / seno(abs(Lt))
    return arctan(result)

def azimut(Lt,lt,Ls,ls):
     #Lt: Latitud terrena // Ls: Latitud satelite
    #lt: longitud terrena // ls: longitud satelite
    alfa=angulo_alfa(Lt,lt,ls)
    # valores Latitud: -90 a 90
    # valores longitud: -180 a 180
    #Revisar posicion terrena
    if Lt>0: # Hemisferio Norte
        
        #El satelite esta mas al norte que la estacion terrena
        if Ls>Lt:
            return -1
        #Satelite al SE de la estacion terrena
        elif ls>lt:
            return 180 - alfa
        #Satelite al SO de la estacion terrena
        elif ls<lt:
            return 180 + alfa

    elif Lt<0: # Hemisferio sur
        
        #Satelite al Sur de la estacion terrena
        if Ls<Lt:
            return -1
        #Satelite al NE
        elif ls>lt : 
            return  alfa
        elif ls<lt:
            return 360 - alfa


# valores Latitud: -90 a 90
# valores longitud: -180 a 180
print('''A continuacion se le solicitan los datos para saber cada ubicacion necesaria. Por favor ingrese los valores en formato decimal utilizando un punto.\n 
        Solo se aceptaran valores entre -90 y 90 para latitud y entre -180 y 180 para longitud. \n En caso de ingresar un formato incorrecto no se podra calcular.''')

T_latitud=input('Ingrese la latitud de la estacion terrena: ').split(' ',1)[0]
T_longitud = input(' Ingrese la longitud de la estacion terrena: ').split(' ',1)[0]
S_latitud= input('Ingrese la latitud del Satelite: ').split(' ',1)[0]
S_longitud = input(' Ingrese la longitud del Satelite: ').split(' ',1)[0]
altura= input(' Ingrese la altura del Satelite: ').split(' ',1)[0]


#Comprobar que los angulos dados esten en el rango aceptado o formatearlos


#Calcular el angulo de elevacion y azimut

#Ver si hay visibilidad entre el satelite y el observador

print(T_latitud,T_longitud,S_latitud,S_longitud,altura)

