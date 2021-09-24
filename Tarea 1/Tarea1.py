# Desarrolle un programa que al ingresar la latitud y longitud en formato decimal de una estación terrena,
#  la latitud y longitud del punto del subsatélite en formato decimal de un satélite GEO y 
# la altura del satélite (en KM ) determine el ángulo de elevación, el Azimut y validar si hay o no visibilidad.

import math as m

def Azimut(Le,le,Ls,ls):
    # Recibe latitud y longitud en angulos 
    # Le: latitud estación terrena.
    # le: longitud estación terrena
    # Ls: latitud satélite
    # ls: longitud satélite

    Le=Le * m.pi/180
    le=le* m.pi/180
    Ls=Ls* m.pi/180
    ls=ls* m.pi/180

    B = ls - le

    alpha = m.atan(m.tan(abs(B))/m.sin(Le))

    #print(alpha*180/m.pi)

   
    if alpha*180/m.pi > -1 and alpha*180/m.pi < 91:  #si esta en NE
        alpha += m.pi
    if alpha < 0:
        alpha = alpha + 2*m.pi
    if Le < 0 and ls > le:
        az = alpha
        return (360-az*180/m.pi)
    if Le < 0 and ls < le:
        az = alpha
        return (az*180/m.pi)



def elevacion(Le,le,Ls,ls,h):
    # Recibe latitud y longitud en angulos 
    # Le: latitud estación terrena.
    # le: longitud estación terrena
    # Ls: latitud satélite
    # ls: longitud satélite
    Le=Le * m.pi/180
    le=le* m.pi/180
    Ls=Ls* m.pi/180
    ls=ls* m.pi/180

    #radio tierra
    re= 6370 #KM
    rs =h + re
    
    gamma=m.acos(m.cos(Le) * m.cos(Ls) * m.cos(ls-le) +  m.sin(Le)*m.sin(Ls) )#en radian

    if m.degrees(gamma) > 81.3:
        print('\t El satelite no es visible')
        elev=m.acos(m.sin(gamma) / m.sqrt( 1 + (re/rs)**2 - (2*(re/rs) * m.cos(gamma)) ))
        return(m.degrees(-elev))
   
    else:
        print('\t El satelite es visible')
        elev=m.acos(m.sin(gamma) / m.sqrt( 1 + (re/rs)**2 - (2*(re/rs) * m.cos(gamma)) ))
        return(m.degrees(elev))



if __name__== "__main__":

    try:
        Le=float(input('|\t Ingrese la LATITUD de la estacion terrena en formato decimal: '))
        le=float(input('|\t Ingrese la LONGITUD de la estacion terrena en formato decimal: '))
        Ls=float(input('|\t Ingrese la LATITUD del satelite en formato decimal: '))
        ls=float(input('|\t Ingrese la LONGITUD del  satelite en formato decimal: '))
        rs=float(input('|\t Ingrese la ALTURA del satelite en KM: '))


        flag= True if (Le>90 or Le<-90) or (Ls>90 or Ls<-90) or (le>180 or le<-180) or (ls>180 or  ls<-180) else False

        while flag:
            print('|\t Hubo un error en los datos ingresados')
            Le=float(input('|\t Ingrese la LATITUD de la estacion terrena en formato decimal: '))
            le=float(input('|\t Ingrese la LONGITUD de la estacion terrena en formato decimal: '))
            Ls=float(input('|\t Ingrese la LATITUD del satelite en formato decimal: '))
            ls=float(input('|\t Ingrese la LONGITUD del  satelite en formato decimal: '))
            rs=float(input('|\t Ingrese la altura del satelite en KM: '))
            flag= True if (Le>90 or Le<-90) or (Ls>90 or Ls<-90) or (le>180 or le<-180) or (ls>180 or  ls<-180) else False
        
        try:
                    
            print('\n|\t El angulo de elevacion es: ',elevacion(Le,le,Ls,ls,rs),'°\n Y el azimut es: ', Azimut(Le,le,Ls,ls))
        except:
            print('Hubo un error en el ingreo de los datos.\nIntente nuevamente')
    
    except:
        print('Hubo un error ingresando los datos. Intente nuevamente.')