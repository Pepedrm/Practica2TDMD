# Definimos los elementos del dominio y del codominio
dominio = ["a", "b", "c", "d"]
codominio = ["a", "b", "c", "d"]

# Función para verificar si una función es monótona creciente
def es_monotona(f):
    # Verificar que f(a) sea "a" o igual a f(b) y f(c) para que se cumpla a <= b y a <= c
    if not (f["a"] == "a" or (f["a"] == f["b"] and f["a"] == f["c"])):
        return False
    # Verificar que f(d) sea mayor o igual que f(b) y f(c)
    if not (f["d"] >= f["b"] and f["d"] >= f["c"]):
        return False
    return True

# Generamos todas las posibles asignaciones del dominio al codominio
def generar_funciones_monotonas():
    funciones = []
    for fa in codominio:
        for fb in codominio:
            for fc in codominio:
                for fd in codominio:
                    f = {"a": fa, "b": fb, "c": fc, "d": fd}
                    if es_monotona(f):
                        funciones.append([(k, v) for k, v in f.items()])
    return funciones

# Imprimir las funciones monótonas crecientes
funciones_monotonas = generar_funciones_monotonas()
print("Funciones monótonas crecientes de dominio a codominio:")
for funcion in funciones_monotonas:
    print(funcion)

# Mostrar el número total de funciones monótonas crecientes encontradas
print(f"Número total de funciones monótonas crecientes: {len(funciones_monotonas)}")
