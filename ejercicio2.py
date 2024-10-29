# Definimos los elementos del dominio y del codominio
dominio = ["a", "b", "c"]
codominio = ["a", "b", "c"]

# Función para verificar si una función es monótona creciente
def es_monotona(f):
    # Comprueba que f["a"] sea "a" o que sea igual a f["b"] y f["c"] para que se cumpla
    # que b<=a y que c<=a
    return (f["a"]=="a" or (f["a"]==f["b"] and f["a"]== f["c"]))

# Generamos todas las posibles asignaciones del dominio al codominio
def generar_funciones_monotonas():
    funciones = []
    for fa in codominio:
        for fb in codominio:
            for fc in codominio:
                f = {"a": fa, "b": fb, "c": fc}
                if es_monotona(f):
                    funciones.append(f)
    return funciones

# Imprimir las funciones monótonas crecientes
funciones_monotonas = generar_funciones_monotonas()
print("Funciones monótonas crecientes de dominio a codominio:")
for funcion in funciones_monotonas:
    print(funcion)

# Mostrar el número total de funciones monótonas crecientes encontradas
print(f"Número total de funciones monótonas crecientes: {len(funciones_monotonas)}")
