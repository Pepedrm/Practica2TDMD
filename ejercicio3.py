def es_reflexiva(P, R):
    """Verifica si la relación es reflexiva."""
    for a in P:
        if (a, a) not in R:
            return False
    return True

def es_antisimetrica(P, R):
    """Verifica si la relación es antisimétrica."""
    for a, b in R:
        if a != b and (b, a) in R:
            return False
    return True

def es_transitiva(P, R):
    """Verifica si la relación es transitiva."""
    for a, b in R:
        for c, d in R:
            if b == c and (a, d) not in R:
                return False
    return True

def es_orden_parcial(P, R):
    """Verifica si la relación es un orden parcial."""
    return es_reflexiva(P, R) and es_antisimetrica(P, R) and es_transitiva(P, R)

def es_dirigido(P, R, A):
    """Verifica si el subconjunto A es dirigido bajo la relación R."""
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            a, b = A[i], A[j]
            encontrado_mayor_comun_superior = False
            for c in P:
                if (a, c) in R and (b, c) in R:
                    encontrado_mayor_comun_superior = True
                    break
            if not encontrado_mayor_comun_superior:
                return False
    return True

def encontrar_supremo(P, R, A):
    """Encuentra el supremo de un subconjunto dirigido A bajo la relación R."""
    posibles_supremos = []
    for c in P:
        if all((a, c) in R for a in A):
            posibles_supremos.append(c)
    
    if not posibles_supremos:
        return None
    
    supremo = posibles_supremos[0]
    for s in posibles_supremos:
        if (s, supremo) in R and s != supremo:
            supremo = s
    return supremo

def es_dcpo(P, R):
    """Verifica si P es un dcpo bajo la relación R."""
    # Verificar si es un orden parcial
    if not es_orden_parcial(P, R):
        return False
    
    # Verificar que cada subconjunto dirigido tiene un supremo
    for tamano_subconjunto in range(2, len(P) + 1):
        subconjuntos_dirigidos = []
        
        # Generar todos los subconjuntos dirigidos de tamaño tamano_subconjunto
        for i in range(len(P)):
            A = P[i:i+tamano_subconjunto]
            if len(A) == tamano_subconjunto and es_dirigido(P, R, A):
                subconjuntos_dirigidos.append(A)
        
        # Verificar que cada subconjunto dirigido tiene un supremo
        for A in subconjuntos_dirigidos:
            if encontrar_supremo(P, R, A) is None:
                return False
    
    return True

def es_continua(P, R, f):
    """Verifica si la función f es continua en el poset P."""
    for tamano_subconjunto in range(2, len(P) + 1):
        subconjuntos_dirigidos = []
        
        # Generar todos los subconjuntos dirigidos de tamaño tamano_subconjunto
        for i in range(len(P)):
            A = P[i:i+tamano_subconjunto]
            if len(A) == tamano_subconjunto and es_dirigido(P, R, A):
                subconjuntos_dirigidos.append(A)
        
        # Verificar la condición de continuidad para cada subconjunto dirigido A
        for A in subconjuntos_dirigidos:
            supremo_A = encontrar_supremo(P, R, A)
            supremo_f_A = encontrar_supremo(P, R, [f[a] for a in A])
            if f[supremo_A] != supremo_f_A:
                return False
    
    return True

def generar_funciones_continuas(P, R):
    """Genera todas las funciones continuas de un poset P en sí mismo."""
    funciones_continuas = []
    n = len(P)
    
    # Generar todas las posibles funciones de P en P
    def generar_asignaciones(actual):
        if len(actual) == n:
            f = {P[i]: actual[i] for i in range(n)}
            if es_continua(P, R, f):
                funciones_continuas.append(f)
            return
        
        for p in P:
            generar_asignaciones(actual + [p])

    generar_asignaciones([])
    return funciones_continuas

def main():
    # Ejemplo de uso
    P = [1, 2, 3]
    R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1, 3)}

    # Verificar si P es un dcpo bajo la relación R
    if es_dcpo(P, R):
        print("El conjunto P es un dcpo.")
        funciones_continuas = generar_funciones_continuas(P, R)
        print("Funciones continuas de P en sí mismo:")
        for f in funciones_continuas:
            print(f)
        print(f"Total de funciones continuas: {len(funciones_continuas)}")
    else:
        print("El conjunto P no es un dcpo.")

if __name__ == "__main__":
    main()
