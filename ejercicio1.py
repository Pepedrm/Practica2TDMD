def es_monotona_creciente(f):
    for i in range(len(f) - 1):
        if f[i] > f[i + 1]:
            return False
    return True

def contar_funciones_monotonas(n, m):
    # Genera todas las posibles funciones monótonas crecientes y las cuenta
    def generar_combinaciones(actual):
        # Si hemos generado una combinación de longitud n, la evaluamos
        if len(actual) == n:
            if es_monotona_creciente(actual):
                return 1
            else:
                return 0
        count = 0
        # Añadimos valores desde 1 hasta m y llamamos recursivamente
        for i in range(1, m + 1):
            count += generar_combinaciones(actual + [i])
        return count

    # Iniciar la recursión con una lista vacía
    return generar_combinaciones([])

def main():
    n = 3
    m = 3
    print(f"Número de funciones monótonas crecientes de P_{n} en P_{m}: {contar_funciones_monotonas(n, m)}")

if __name__ == "__main__":
    main()
