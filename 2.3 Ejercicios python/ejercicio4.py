asignatura_nueva = ["Fisica"]
def agregar_asignatura(funcion):
   asig_nueva = input("Ingrese la asignatura: ")
   if asig_nueva == "exit" :
       return funcion
   else:
       return agregar_asignatura(funcion + [asig_nueva])
    
    


print(agregar_asignatura(asignatura_nueva))