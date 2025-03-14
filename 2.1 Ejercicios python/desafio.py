total_redes = 0
total_BD = 0
total_DesarrolloSoftware = 0
total_ProgramacionHardware = 0
total_Modelado3D = 0
total_GestionProyectosSoftware = 0

def main():
    global total_redes, total_BD, total_DesarrolloSoftware, total_ProgramacionHardware, total_Modelado3D, total_GestionProyectosSoftware
    
    print("Bienvenido al cuestionario de intereses en sistemas computacionales.")
    print("Por favor, responde las siguientes preguntas con 'sí' o 'no'.")

    preguntas = [
        "¿Te interesa la configuración y administración de redes?",
        "¿Te gusta trabajar con bases de datos y gestionar grandes volúmenes de información?",
        "¿Te apasiona el desarrollo de software y la creación de aplicaciones?",
        "¿Te interesa la programación de hardware y el desarrollo de sistemas embebidos?",
        "¿Te gusta el modelado 3D y la creación de gráficos por computadora?",
        "¿Te interesa la gestión de proyectos de software y la coordinación de equipos de desarrollo?"
    ]

    respuestas = []

    for pregunta in preguntas:
        respuesta = input(pregunta + " ")
        respuestas.append(respuesta.lower())

    for i, respuesta in enumerate(respuestas):
        if i == 0 and respuesta == 'si':
            total_redes += 1
        elif i == 1 and respuesta == 'si':
            total_BD += 1
        elif i == 2 and respuesta == 'si':
            total_DesarrolloSoftware += 1
        elif i == 3 and respuesta == 'si':
            total_ProgramacionHardware += 1
        elif i == 4 and respuesta == 'si':
            total_Modelado3D += 1
        elif i == 5 and respuesta == 'si':
            total_GestionProyectosSoftware += 1
               
            

    continuar = input("¿Desea otro estudiante realizar el cuestionario? (sí/no): ").lower()
    if continuar == 'si':
        main()
    else:
        print("\nResumen de intereses de todos los estudiantes:")
        print(f"Intereses en Redes: {total_redes}")
        print(f"Intereses en Bases de Datos: {total_BD}")
        print(f"Intereses en Desarrollo de Software: {total_DesarrolloSoftware}")
        print(f"Intereses en Programación Hardware: {total_ProgramacionHardware}")
        print(f"Intereses en Modelado 3D: {total_Modelado3D}")
        print(f"Intereses en Gestión de Proyectos de Software: {total_GestionProyectosSoftware}")
        return
    

    
    intereses = {
        "Redes": respuestas[0] == 'si'  ,
        "Bases de Datos": respuestas[1] == 'si',
        "Desarrollo de Software": respuestas[2] == 'si',
        "Programación Hardware": respuestas[3] == 'si',
        "Modelado 3D": respuestas[4] == 'si',
        "Gestión de Proyectos de Software": respuestas[5] == 'si'
        
    }

           
    
          

           
main()
