#-*- coding:utf-8 -*-
caracteres_encriptados = {'a':1,'b':2,'c':"c",'d':4,'e':"e",'f':6,'g':7,'h':8,'i':"i",'j':0,'k':11,'l':12,'m':13,'n':14,'o':"o",'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,"/":"a","*":"e","-":"i","+":"j"}
encriptada = ""
#Crear usuario y clave
print("\n         .:Bienvenido:.\nPara empezar, debe crear un usuario")
user=input("Ingrese un nombre de usuario: ")
while True: 
    #Hacer que la contraseña cumpla con los requisitos
    pswr = input("Ingrese una contraseña\nCaracteres permitidos: (Aa-Zz, 0-9, /,*,-,+): ")
    longitud_clave = len(pswr) #verificar la longitud de la clave
    if longitud_clave >= 8 and longitud_clave <=10  and "/" in pswr or "*" in pswr or "-" in pswr or "+" in pswr:
        print("Contraseña aceptada")
        break
    else:
        print("La contraseña debe tener una longitud entre 8 y 10 caracteres.") 
key_encript = ''
#Encriptar por sustitucion
for letra in pswr:
    nLetra = caracteres_encriptados.get(letra) if letra in caracteres_encriptados else letra
    key_encript = '%s%s' % (key_encript, nLetra)
#Fin crear usuario
clients = {}    #Base de datos

while True:
    #Inicio Menu de opciones
    print ("\n        *** Menu Principal ***")
    print ("1- Añadir cliente           2- Eliminar cliente") 
    print ("3- Mostrar cliente          4- Listar todos los clientes")
    print ("5- Clientes de tercera edad")
    print ("6- Terminar") #Fin Menu de opciones
    opc = int(input("\nIngrese una opcion: "))  #Escoger una opcion del menu
    if opc == 1:
        print(">",user)
        #Pedir los daots al usuario
        while True: #Comprobar que el usuario solo ingrese numeros en la cedula
            try:
                ci=int(input("Introduzca la cedula del cliente: ")) #Pedir la cedula             
                if ci >= 7000000 and ci <= 33000000:    #Comprobar que la cedula este en un rango correcto
                    break
                elif ci > 33000000 and ci <= 38999999: #Es menor de edad
                    print(f"La persona es menor de edad, no puede ingresar a la empresa.")
                elif ci >= 39000000: #Excede el rango
                    print(f"La cedula ingresada exede el rango")
                else:
                    print("Cedula incorrecta, tal vez ya no exista XD")
            except ValueError:  #Mostrar el error
                print("Debes ingresar un numero de cedula")
        nif = str(ci) #Convertir la cedula a cadena para que no de problema en las iteraciones
        nombre = input("Nombre: ")
        #Calcular edad
        year=2023
        anac=int(input("Ingrese su año de nacimiento: "))
        mnac=int(input("Ingrese su mes de nacimiento: "))
        dnac=int(input("Ingrese su dia de nacimiento: "))
        edad = year - anac
        #Hacer que solo ingrese una de las 3 opciones
        while True:
            sexo = input("Sexo(Femenino, Masculino, Otro): ")
            sexo=sexo.lower()
            if sexo == "femenino" or sexo == "masculino" or sexo == "otro":
                break   #Si esta entre las opciones, sale de la condicion y continua
            else:
                print("No esta entre las opciones")
        direccion = input("Direccion: ")
        while True: #Comprobar que el usuario solo ingrese numeros en el telefono
                try:
                    telefono=int(input("Introduzca su numero de telefono: ")) #Pedir numero de telefono           
                    break
                except ValueError:  #Mostrar el error
                    print("Debe ingresar un numero de telefono")
        correo = input("Correo: ")    
        if sexo == "masculino" and edad >= 60 or sexo == "femenino" and edad >= 55:
            trat = "Tercera edad"
        else:
            trat="N/A"
        #Crear lista para añadir los datos
        clientes= {"Nombre":nombre,"Sexo":sexo,"Direccion":direccion,"Telefono":telefono,"Correo":correo,"Fecha de nacimiento":[dnac,mnac,anac],"Edad":edad,"Trato":trat} 
        clients[nif]=clientes   #La clave es la cedula y el valor la lista, se añade el cliente
        print("Cliente registrado")
    elif opc == 2:  #Eliminar un cliente
        print(">",user)
        p_nif=str(input("\n.:Eliminar cliente:. \nIngrese la cedula del cliente que desea eliminar: "))
        valor=clients.get(p_nif)
        if valor!=None:
            eliminar=clients.pop(p_nif)
            print("Cliente eliminado")
        else:
             print("No se encuentra registrado")
             continue
    elif opc == 3:  #Mostrar un cliente
            print(">",user)
            p_nif=str(input("\n.:Mostrar cliente:.\nIngrese la cedula del cliente: "))
            valor=clients.get(p_nif)
            if valor!=None:
                print("***************************")
                print("C.I: :",p_nif)
                for z in clients[p_nif]:
                    print(z,":",clients[p_nif][z]) 
            else:
                print("no existe ese NIF")
                continue
    elif opc == 4:  #Mostrar todos los clientes
        print(">",user)
        print("\n.:Mostrar todos los cliente:.")
        for x in clients:
            print("*********************")
            print("Cedula: ", x)
            for z in clients[x]:
                print(z,":",clients[x][z])
    elif opc == 5:  #Mostrar los de tercera edad
       print(">",user)
       print("\n.:Clientes de tercera edad y preferentes:.\n")
       for x in clients:
           for z in clients[x].items():
               if "Tercera edad" in z:
                   for y in clients [x].items():
                       if "Nombre" in y:
                        clave = y[0]
                        valor = y[1]
                        print("Cedula: "+x+" "+clave+":"+valor+"\n")
    elif opc == 6:  #Terminar el programa mostrando los integrantes
        print("Elaborado por\n-Jhon Lopez\n-Reiner Gamboa\n-Reiner Nogales\n-Jorge Rodriguez\n-Daniel Romero")
        print("Contraseña encriptada",key_encript)
        break        
    else:  #la opcion no esta en el menu
     print("Esta opcion no esta disponible\n")