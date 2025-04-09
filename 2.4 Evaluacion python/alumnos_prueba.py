from functools import reduce

# Tipos de aspectos a evaluar
ASIGNATURAS = ["Matemáticas", "Lengua", "Ciencias", "Historia"]
ASPECTOS = ["Actividades", "Herramientas", "Contenido", "Evaluación", "Material Didáctico"]

# ---------------------- Funciones puras ----------------------


def ingresar_calificaciones(aspectos, alumno):
    """
    Solicita    al usuario ingresar calificaciones para cada aspecto, mostrando el nombre del alumno.
    """
    return list(map(lambda aspecto: ingresar_calificaciones_por_aspecto(aspecto, alumno), aspectos))

def ingresar_calificaciones_por_aspecto(aspecto, alumno):
    """
    Solicita al usuario ingresar calificaciones numéricas (0-10) separadas por coma,
    indicando el alumno actual.
    """
    calificaciones_str = input(f"Ingrese las calificaciones de {alumno} para '{aspecto}': ")
    return list(map(int, calificaciones_str.split(",")))

def promedio(lista):
    """
    Calcula el promedio de una lista de números.
    """
    return reducir_suma(lista) / len(lista) if lista else 0

def reducir_suma(lista):
    """
    Suma los elementos de una lista usando reduce.
    """
    return reduce(lambda x, y: x + y, lista, 0)

def calcular_metricas(calificaciones):
    """
    Calcula promedios y totales por aspecto.
    Retorna una lista de tuplas (aspecto, promedio, total).
    """
    return list(map(lambda par: (par[0], promedio(par[1]), reducir_suma(par[1])), zip(ASPECTOS, calificaciones)))

def filtrar_mayores_a(calificaciones, umbral):
    """
    Filtra las calificaciones mayores a un umbral.
    """
    return list(filter(lambda x: x > umbral, calificaciones))

def calcular_promedio_general(calificaciones):
    """
    Calcula el promedio general de todas las calificaciones de una asignatura.
    """
    todas = sum(calificaciones, [])  # Aplana la lista de listas
    return promedio(todas), reducir_suma(todas)


# ---------------------- Recursividad ----------------------

def imprimir_resultados_recursivo(resultados, i=0):
    """
    Imprime recursivamente los resultados de la encuesta.
    """
    if i >= len(resultados):
        return
    aspecto, prom, total = resultados[i]
    print(f"{aspecto}: Promedio = {prom:.2f}, Total = {total}")
    imprimir_resultados_recursivo(resultados, i + 1)

def combinar_calificaciones_por_aspecto(lista_de_calificaciones):
    """
    Combina las calificaciones de múltiples alumnos por aspecto usando comprensión de listas.
    """
    return [sum(aspecto, []) for aspecto in zip(*lista_de_calificaciones)]

def asociar_calificaciones_con_asignaturas(asignaturas, calificaciones_lista):
    """
    Asocia cada conjunto de calificaciones con un alumno y su asignatura.
    Retorna una lista de tuplas (alumno, asignatura, calificaciones_por_aspecto).
    """
    return list(map(lambda i: (f"Alumno {i+1}", asignaturas[i], calificaciones_lista[i]), range(len(asignaturas))))



# ---------------------- Main ----------------------

def main():
    print("=== Encuesta de Evaluación de Asignaturas ===")

    # Recolectar calificaciones mostrando el nombre del alumno
    alumnos = [f"Alumno {i+1}" for i in range(len(ASIGNATURAS))]
    calificaciones_todos = list(map(lambda par: ingresar_calificaciones(ASPECTOS, par[0]), zip(alumnos, ASIGNATURAS)))

    # Asociar alumno, asignatura y calificaciones
    asociaciones = asociar_calificaciones_con_asignaturas(ASIGNATURAS, calificaciones_todos)

    resultados_por_asignatura = list(map(
    lambda asociacion: (
        asociacion[0],  # Alumno
        asociacion[1],  # Asignatura
        calcular_promedio_general(asociacion[2])  # (promedio, total)
    ),
    asociaciones
))

    # Imprimir resultados
    list(map(
    lambda resultado: print(
        f"\n--- Resultados de {resultado[0]} para la asignatura: {resultado[1]} ---\n" +
        f"Promedio General = {resultado[2][0]:.2f}, Total = {resultado[2][1]}"
    ),   resultados_por_asignatura))



if __name__ == "__main__":
    main()
