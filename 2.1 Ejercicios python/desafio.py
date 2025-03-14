def main():
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

    total_redes = 0
    total_BD = 0
    total_DesarrolloSoftware = 0
    total_ProgramacionHardware = 0
    total_Modelado3D = 0
    total_GestionProyectosSoftware = 0

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
            
                
            

       
    

    
    intereses = {
        "Redes": respuestas[0] == 'si'  ,
        "Bases de Datos": respuestas[1] == 'si',
        "Desarrollo de Software": respuestas[2] == 'si',
        "Programación Hardware": respuestas[3] == 'si',
        "Modelado 3D": respuestas[4] == 'si',
        "Gestión de Proyectos de Software": respuestas[5] == 'si'
    }

    print("\nTus intereses en sistemas computacionales son:")
    for area, interesado in intereses.items():
        if interesado:
            if area == "Redes":
                print(f"- {area} (Total: {total_redes})")
            elif area == "Bases de Datos":
                print(f"- {area} (Total: {total_BD})")
            elif area == "Desarrollo de Software":
                print(f"- {area} (Total: {total_DesarrolloSoftware})")
            elif area == "Programación Hardware":
                print(f"- {area} (Total: {total_ProgramacionHardware})")
            elif area == "Modelado 3D":
                print(f"- {area} (Total: {total_Modelado3D})")
            elif area == "Gestión de Proyectos de Software":
                print(f"- {area} (Total: {total_GestionProyectosSoftware})")

main()
