"""se importa la funciones"""
from suma import suma 
from resta import resta

"""se crea el menu"""
bandera = True 
while bandera: 
    print("\nBienvenid@ a la calculadora")
    print("por favor escoga una de las siguientes opciones: ")
    print("1 - para sumar")
    print("2 - para restar")
    print("3 - para multiplicarr")
    print("4 - para dividir")
    print("0 - para salir")
    try:
        opcion = int(input("\nPor favor digite la opcion: "))
        if(opcion == 0):
            bandera = False
            print("Muchas gracias")
        else:
            try: 
                numeroa = float(input("Ingrese numeroa: "))
                try: 
                    numerob = float(input("Ingresa numerob: "))
                    if(opcion == 1):
                        print("La suma de los numeroa y numerob es: "+str(suma(numeroa,numerob)))
                    elif(opcion == 2):
                        print("La resta de los numeroa y numerob es: "+str(resta(numeroa,numerob)))
                except ValueError:
                    print("El numero ingresado no es un flotante")  
            except ValueError:
                print("El numero ingresado no es un flotante") 

    except ValueError:
        print("El numero ingresado no es un entero ingreselo de nuevo por favor")