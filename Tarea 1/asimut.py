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

    #print(Le,le,Ls,ls)

    B = ls - le

    alpha = m.atan(m.tan(abs(B))/m.sin(Le))

    alpha += m.pi # borrar e ir probando 

    print(B)
    print(alpha)

    if Le < 0 and B < 0:
        az = alpha
        print(az*180/m.pi)
    if Le < 0 and B > 0:
        az = 2*m.pi - alpha
        print(az*180/m.pi)
    if Le > 0 and B < 0:
        az = m.pi + alpha
        print(az*180/m.pi)
    if Le > 0 and B > 0:
        az = m.pi - alpha
        print(az*180/m.pi)



elevacion(-33.42,-70.56,1.81,80.04,35789.91)

#print(m.atan(-1)*180/m.pi)