# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18vqLnHsYfkeXhGv-BPlKAOHuTf-hSjuP
"""

print("Bienvenidos a Pizza Express")
print("Cuando tu placer se esconde en la pizza")
nombre = str (input ("¿Con quien tenemos el gusto?"))
print("Bienvenido" +nombre)
print("Le agradecemos nos regale su información para poder hacerle llegar su pedido")
provincia = str(input("Provincia:"))
barrio = str(input("Barrio:"))
calle = str(input("Calle:"))
casa = str(input("Casa o apartamento:"))
numcasa = str(input("Numero de casa o apartamento:"))
instrucciones = str(input("Instrucciones de entrega para el repartidor:"))
print("Muchas gracias por la información" +nombre)
print("Iniciaremos con el pedido")
print("Escoja el tamaño de pizza que desea:")
print("""
    1) Regular (10 pulgadas)       
    2) Familiar (14 pulgadas)
    3) Xtra Grande (18 pulgadas)
    """)
tamaño=input("Escriba el numero:")
regular=7.50
familiar=9.99
xtra_grande=12.50
if (tamaño=="1"):
  print("""
        Escoja su pizza Regular favorita:

    1) Queso          5)Hongos      
    2) Pepperoni      6)Hawaina
    3) Pollo          7)Express Special
    4) Combinación 
    """)
  sabor_regular=input("Escriba el numero:")
  if (sabor_regular=="1"):
    print("Su pizza Regular de Queso tiene un valor de: $" +str(regular))
    valor_pizza=regular
  elif sabor_regular=="2":
    print("Su pizza Regular de Pepperoni tiene un valor de: $" +str(regular))
    valor_pizza=regular
  elif sabor_regular=="3":
    print("Su pizza Regular de Pollo tiene un valor de: $" +str(regular))
    valor_pizza=regular
  elif sabor_regular=="4":
    print("Su pizza Regular de Combinación tiene un valor de: $" +str(regular))
    valor_pizza=regular
  elif sabor_regular=="5":
    print("Su pizza Regular de Hongos tiene un valor de: $" +str(regular))
    valor_pizza=regular
  elif sabor_regular=="6":
    print("Su pizza Regular Hawaina tiene un valor de: $" +str(regular))
    valor_pizza=regular
  elif sabor_regular=="7":
    print("Su pizza Regular Express Special tiene un valor de: $" +str(regular))
    valor_pizza=regular
if(tamaño=="2"):
  print("""
        Escoja su pizza Familiar favorita:

    1) Queso          5)Hongos      
    2) Pepperoni      6)Hawaina
    3) Pollo          7)Express Special
    4) Combinación 
    """)
  sabor_familiar=input("Escriba el numero:")
  if (sabor_familiar=="1"):
    print("Su pizza Familiar de Queso tiene un valor de: $" +str(familiar))
    valor_pizza=familiar
  elif sabor_familiar=="2":
    print("Su pizza Familiar de Pepperoni tiene un valor de: $" +str(familiar))
    valor_pizza=familiar
  elif sabor_familiar=="3":
    print("Su pizza Familiar de Pollo tiene un valor de: $" +str(familiar))
    valor_pizza=familiar
  elif sabor_familiar=="4":
    print("Su pizza Familiar de Combinación tiene un valor de: $" +str(familiar))
    valor_pizza=familiar
  elif sabor_familiar=="5":
    print("Su pizza Familiar de Hongos tiene un valor de: $" +str(familiar))
    valor_pizza=familiar
  elif sabor_familiar=="6":
    print("Su pizza Familiar Hawaina tiene un valor de: $" +str(familiar))
    valor_pizza=familiar
  elif sabor_familiar=="7":
    print("Su pizza Familiar Express Special tiene un valor de: $" +str(familiar))
    valor_pizza=familiar
if(tamaño=="3"):
  print("""
        Escoja su pizza Xtra Grande favorita:

    1) Queso          5)Hongos      
    2) Pepperoni      6)Hawaina
    3) Pollo          7)Express Special
    4) Combinación 
    """)
  sabor_xtra_grande=input("Escriba el numero:")
  if (sabor_xtra_grande=="1"):
    print("Su pizza Xtra Grande de Queso tiene un valor de: $" +str(xtra_grande))
    valor_pizza=xtra_grande
  elif sabor_xtra_grande=="2":
    print("Su pizza Xtra Grande de Pepperoni tiene un valor de: $" +str(xtra_grande))
    valor_pizza=xtra_grande
  elif sabor_xtra_grande=="3":
    print("Su pizza Xtra Grande de Pollo tiene un valor de: $" +str(xtra_grande))
    valor_pizza=xtra_grande
  elif sabor_xtra_grande=="4":
    print("Su pizza Xtra Grande de Combinación tiene un valor de: $" +str(xtra_grande))
    valor_pizza=xtra_grande
  elif sabor_xtra_grande=="5":
    print("Su pizza Xtra Grande de Hongos tiene un valor de: $" +str(xtra_grande))
    valor_pizza=xtra_grande
  elif sabor_xtra_grande=="6":
    print("Su pizza Xtra Grande Hawaina tiene un valor de: $" +str(xtra_grande))
    valor_pizza=xtra_grande
  elif sabor_xtra_grande=="7":
    print("Su pizza Xtra Grande Express Special tiene un valor de: $" +str(xtra_grande))
    valor_pizza=xtra_grande
print("""
        Escoja su refresco de preferencia:

    1) Coca-Cola     4)Fanta      
    2) Sprite        5)Fresa
    3) Ginger Ale 
    """)
bebida=input("Escriba el numero:")
lata=1.25
litro_1=1.75
litro_2=3.25
if (bebida=="1"):
  print("""
        Escoja el tamaño de su Coca-Cola:

    1) Lata (600ml)      
    2) 1 litro
    3) 2 litros  
    """)
  tamaño_coca=input("Escriba el numero:")
  if (tamaño_coca=="1"):
    print("Su refresco de Lata (600ml) de Coca-Cola tiene un valor de: $" +str(lata))
    valor_soda=lata
  elif tamaño_coca=="2":
    print("Su refresco de 1 litro de Coca-Cola tiene un valor de: $" +str(litro_1))
    valor_soda=litro_1
  elif tamaño_coca=="3":
    print("Su refresco de 2 litro de Coca-Cola tiene un valor de: $" +str(litro_2))
    valor_soda=litro_2
if (bebida=="2"):
  print("""
        Escoja el tamaño de su Sprite:

    1) Lata (600ml)      
    2) 1 litro
    3) 2 litros  
    """)
  tamaño_sprite=input("Escriba el numero:")
  if (tamaño_sprite=="1"):
    print("Su refresco de Lata (600ml) de Sprite tiene un valor de: $" +str(lata))
    valor_soda=lata
  elif tamaño_sprite=="2":
    print("Su refresco de 1 litro de Sprite tiene un valor de: $" +str(litro_1))
    valor_soda=litro_1
  elif tamaño_sprite=="3":
    print("Su refresco de 2 litro de Sprite tiene un valor de: $" +str(litro_2))
    valor_soda=litro_2
if (bebida=="3"):
  print("""
        Escoja el tamaño de su Ginger Ale:

    1) Lata (600ml)      
    2) 1 litro
    3) 2 litros  
    """)
  tamaño_ginger=input("Escriba el numero:")
  if (tamaño_ginger=="1"):
    print("Su refresco de Lata (600ml) de Ginger Ale tiene un valor de: $" +str(lata))
    valor_soda=lata
  elif tamaño_ginger=="2":
    print("Su refresco de 1 litro de Ginger Ale tiene un valor de: $" +str(litro_1))
    valor_soda=litro_1
  elif tamaño_ginger=="3":
    print("Su refresco de 2 litro de Ginger Ale tiene un valor de: $" +str(litro_2))
    valor_soda=litro_2
if (bebida=="4"):
  print("""
        Escoja el tamaño de su Fanta:

    1) Lata (600ml)      
    2) 1 litro
    3) 2 litros  
    """)
  tamaño_fanta=input("Escriba el numero:")
  if (tamaño_fanta=="1"):
    print("Su refresco de Lata (600ml) de Fanta tiene un valor de: $" +str(lata))
    valor_soda=lata
  elif tamaño_fanta=="2":
    print("Su refresco de 1 litro de Fanta tiene un valor de: $" +str(litro_1))
    valor_soda=litro_1
  elif tamaño_fanta=="3":
    print("Su refresco de 2 litro de Fanta tiene un valor de: $" +str(litro_2))
    valor_soda=litro_2
if (bebida=="5"):
  print("""
        Escoja el tamaño de su Fresa:

    1) Lata (600ml)      
    2) 1 litro
    3) 2 litros  
    """)
  tamaño_fresa=input("Escriba el numero:")
  if (tamaño_fresa=="1"):
    print("Su refresco de Lata (600ml) de Fresa tiene un valor de: $" +str(lata))
    valor_soda=lata
  elif tamaño_fresa=="2":
    print("Su refresco de 1 litro de Fresa tiene un valor de: $" +str(litro_1))
    valor_soda=litro_1
  elif tamaño_fresar=="3":
    print("Su refresco de 2 litro de Fresa tiene un valor de: $" +str(litro_2))
    valor_soda=litro_2
sub_total=(valor_pizza+valor_soda)
itbms= (sub_total*0.07)
total= (sub_total+itbms)
print("Muchas gracias por escoger a Pizza Express " +nombre)
print("Su pedido sera enviado a: " +provincia +", " +barrio +", calle:" +calle +", " +casa +"#" +numcasa)
print ("Utilizaremos esta referencia: " +instrucciones)
print("Subtotal: %.2f$" %(sub_total))
print("ITBMS:     %.2f$" %(itbms))
print("Total:    %.2f$" %(total))
print("Gracias por preferirnos " +nombre)
print("Cuentanos cómo ha sido tu experiencia en Pizza Express, y participa en el sorteo de 3 iPad mini.")
print("Visita www.PizzaExpress.com.pa")