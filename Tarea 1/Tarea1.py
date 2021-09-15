# Desarrolle un programa que al ingresar la latitud y longitud en formato decimal de una estación terrena,
#  la latitud y longitud del punto del subsatélite en formato decimal de un satélite GEO y 
# la altura del satélite (en KM ) determine el ángulo de elevación, el Azimut y validar si hay o no visibilidad.

import math as m


def elevacion(Le,le,Ls,ls,rs):
    # Recibe latitud y longitud en angulos 
    # Le: latitud estación terrena.
    # le: longitud estación terrena
    # Ls: latitud satélite
    # ls: longitud satélite
    Le=Le * m.pi/180
    le=le* m.pi/180
    Ls=Ls* m.pi/180
    ls=ls* m.pi/180

    print(Le,le,Ls,ls)
    
    #Calcular gamma segun la ecuacion 1
    # 1.- cos(gamma) = cos(Le)*cos(Ls)*cos(ls-le)+sin(Le)*sin(Ls)
    cos_gamma = (m.cos(Le) * m.cos(Ls) * m.cos(ls-le)) + ( m.sin(Le)*m.sin(Ls) )
    gamma=m.acos(cos_gamma)#en radian

    print('coseno: ', cos_gamma, 'gamma: ', gamma )

    #radio tierra
    re= 6378.137 #KM
    #Calcular elevacion segun ecuacion 2
    #2.- cos(El) = sin(gamma) / (1+ (re/rs)**2 - 2(re/rs)*cos_gamma)**2
    cos_elev = m.sin(gamma) / ( 1 + (re/rs)**2 - (2*(re/rs) * m.cos(gamma)) )**0.5 
    elev=m.acos(cos_elev)
    print('coseno: ', cos_elev, 'elev ', elev )

    print('grados:', m.degrees(elev))


elevacion(-33.42,-70.56,-0.08,98.06,35789.91)
