# -*- coding: utf-8 -*-
import numpy as np
asientosN=np.array(
    [
     [1,2,3,4,5,6],
     [7,8,9,10,11,12],
     [13,14,15,16,17,18],
     [19,20,21,22,23,24],
     [25,26,27,28,29,30]
     ]
    )

asientosV=np.array(
    [
     [31,32,33,34,35,36],
     [37,38,39,40,41,42]
     ]
    )

datos=[]
total=0
# x="x"
def asientosDis (opcion):
  if opcion==1:
    print(np.concatenate((asientosN, asientosV), axis=0))
 
asientosDis(1)

def comprarAsi (opcion):
  if opcion==2:
    print("Ingrese sus datos")
    datos=[]
    nombre=input("ingrese su nombre")
    datos.append(nombre)
    rut=input("ingrese su rut")
    datos.append(rut)
    telefono=int(input("ingrese su numero celular"))
    datos.append(telefono)
    
    banco=input("ingrese su banco, si pertenece a banco Duoc presione uno para obtener un descuento")
    # if banco=='1':
      # total*=0.15

    datos.append(banco)

    print("escoja uno de los asientos disponible")
    print(np.concatenate((asientosN, asientosV), axis=0))
    comprado=int(input())
    



    asientosN





    print(datos)

comprarAsi(2)
