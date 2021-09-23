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

    #radio tierra
    re= 6370 #KM
    rs+=re
    print(Le,le,Ls,ls)
    
    #Calcular gamma segun la ecuacion 1
    # 1.- cos(gamma) = cos(Le)*cos(Ls)*cos(ls-le)+sin(Le)*sin(Ls)
    # cos_gamma = (m.cos(Le) * m.cos(Ls) * m.cos(ls-le)) + ( m.sin(Le)*m.sin(Ls) )
    gamma=m.acos(m.cos(Le) * m.cos(Ls) * m.cos(ls-le) +  m.sin(Le)*m.sin(Ls) )#en radian
    # gamma = np.arccos( np.cos(np.deg2rad(Le))*np.cos(np.deg2rad(Ls))*np.cos(np.deg2rad(ls-le)) + np.sin(np.deg2rad(Le))*np.sin(np.deg2rad(Ls)) )
    # print('gamma: ', m.degrees(gamma))

    if m.degrees(gamma) > 81.3:
        print('El satelite no es visible')
        elev=m.acos(m.sin(gamma) / m.sqrt( 1 + (re/rs)**2 - (2*(re/rs) * m.cos(gamma)) ))
        # elevation = np.arccos( np.sin(np.deg2rad(gamma)) / np.sqrt(1+(6378.137/rs)**(2) -2*(6378.137/rs)*np.cos(np.deg2rad(gamma))) )
        # print('elevacion con acos: ', elev )

        print('elevacion en grados:', m.degrees(-elev))
        azimut(Le,le,ls,gamma)

        
    else:
        print('el satelite es visible')
        
        #Calcular elevacion segun ecuacion 2
        #2.- cos(El) = sin(gamma) / (1+ (re/rs)**2 - 2(re/rs)*cos_gamma)**2
        # cos_elev = m.sin(gamma) / ( 1 + (re/rs)**2 - (2*(re/rs) * m.cos(gamma)) )**0.5
        
        elev=m.acos(m.sin(gamma) / m.sqrt( 1 + (re/rs)**2 - (2*(re/rs) * m.cos(gamma)) ))
        # elevation = np.arccos( np.sin(np.deg2rad(gamma)) / np.sqrt(1+(6378.137/rs)**(2) -2*(6378.137/rs)*np.cos(np.deg2rad(gamma))) )
        # print('elevacion con acos: ', elev )

        print('elevacion en grados:', m.degrees(elev))

def azimut(Le,le,ls,gamma):
    
    alpha = m.atan(m.tan(abs(ls-le))/m.sin(Le))
    # print(alpha,'   debe ser entre 0 y pi')

    if m.degrees(gamma)>81.3:#El satelite no es visible
        alpha += m.pi # borrar e ir probando 
        # print(alpha,'   debe ser entre 0 y pi')
    
    

    if Le < 0 :
        az = abs(alpha)
        # print(az*180/m.pi)
    if Le < 0 :
        az = 2*m.pi - abs( alpha)
        # print(az*180/m.pi)
    if Le > 0:
        az = m.pi + abs(alpha)
        # print(az*180/m.pi)
    if Le > 0:
        az = m.pi - abs( alpha)
        # print(az*180/m.pi)

    print('azimut: ' , m.degrees(az))
    




# elevacion(-33.03932,-71.62725,-0.03,83.08,35808.61)#-54.3
# elevacion(-33.03932,-71.62725,0.00,128.27,3577.21)#-56.8
# elevacion(-33.03932,-71.62725,0.03,-100.85,35787.5)#40.4
# elevacion(-33.03932,-71.62725,0.00,17.01,35794.51)#-6.6 AZ=88.7 E
# elevacion(-33.03932,-71.62725,-0.32,87.33,35783.83)#-55.3 Az=143.9 SE
# elevacion(-33.03932,-71.62725,-1.90,-98.00,35778.41)#43 da 42.711
# elevacion(-33.03932,-71.62725,7.75,-169.55,35991.82)#-19.9 da 20.39


# elevacion(-32.83369,-70.59827,-0.18,87.40,35771.53)


# elevacion(-33.42628,-70.59827,0.04,-100.86,35787.76)
# azimut(-33.42628,-70.59827,0.04,-100.86)

# elevacion(-32.83369,-70.59827,-0.99,-68.58,35708.96)
# azimut(-32.83369,-70.59827,-0.99,-68.58)


if __name__== "__main__":
    Le,le =  -32.83369,-70.59827
    Ls,ls = -0.02,61.94
    rs= 35785.90

    flag= True if (Le>90 or Le<-90) or (Ls>90 or Ls<-90) or (le>180 or le<-180) or (ls>180 or  ls<-180) else False

    while flag:
        print('hubo un error en los datos ingresados')
        flag=False
    

    elevacion(Le,le,Ls,ls,rs)

