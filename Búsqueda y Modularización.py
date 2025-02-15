import random
import string
import timeit # Permiso

# Clase para el usuario
class Usuario:
    def __init__(self, user_id, nombre, edad):
        self.user_id = user_id
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"Usuario(ID={self.user_id}, Nombre={self.nombre}, Edad={self.edad})"

# Generar 100,000 usuarios con datos aleatorios
def generar_usuarios(cantidad):
    usuarios = []
    for user_id in range(1, cantidad + 1):
        nombre = ''.join(random.choices(string.ascii_letters, k=8))  # Nombre aleatorio de 8 letras
        edad = random.randint(18, 99)  # Edad aleatoria entre 18 y 99
        usuarios.append(Usuario(user_id, nombre, edad)) # Crea un usuaria y lo agrega a la lista
    return usuarios

# Búsqueda lineal
def busqueda_lineal(usuarios, user_id):
    for usuario in usuarios: # Recorre la lista uno por uno
        if usuario.user_id == user_id: # Verifica ID
            return usuario # Retorna si se encuentra
    return None # Retornar none si no se encuentra

# Búsqueda binaria (requiere lista ordenada por ID)
def busqueda_binaria(usuarios, user_id):
    inicio, fin = 0, len(usuarios) - 1 # establece limetes en la lista
    while inicio <= fin: # no se cruzan los limites
        medio = (inicio + fin) // 2 # ENCUENTRA EL PUNTO MEDIO
        if usuarios[medio].user_id == user_id: # SI EL ID ESTA EN MEDIO
            return usuarios[medio]
        elif usuarios[medio].user_id < user_id: # SI EL ID BUSCADO ES MAYOR
            inicio = medio + 1 # MUEVE EL LIMITE INFERIOR
        else: # SI EL ID ES MENOR
            fin = medio - 1 # MUEVE A LIMITE SUPERIOR
    return None

# Ordenar la lista de usuarios para la búsqueda binaria
def ordenar_usuarios(usuarios):
    return sorted(usuarios, key=lambda x: x.user_id) # ORDENA POR EL ID

# Función para comparar tiempos
def comparar_tiempos(user_id, usuarios, usuarios_ordenados):
    tiempo_lineal = timeit.timeit(lambda: busqueda_lineal(usuarios, user_id), number=1)
    tiempo_binario = timeit.timeit(lambda: busqueda_binaria(usuarios_ordenados, user_id), number=1)
    return tiempo_lineal, tiempo_binario

# INICIO DEL PROGRAMA
if __name__ == "__main__":
    print("Generando 100,000 usuarios...")
    usuarios = generar_usuarios(100000)
    usuarios_ordenados = ordenar_usuarios(usuarios) # ORDENA LOS USUARIOS

    user_id_buscado = random.randint(1, 100000)  # Buscar un ID aleatorio
    print(f"Buscando el usuario con ID={user_id_buscado}")

    # COMPARA TIEMPOS
    tiempo_lineal, tiempo_binario = comparar_tiempos(user_id_buscado, usuarios, usuarios_ordenados)
    print(f"Tiempo de búsqueda lineal: {tiempo_lineal:.6f} segundos")
    print(f"Tiempo de búsqueda binaria: {tiempo_binario:.6f} segundos")

    # MUESTRA RESULTADOS
    usuario_encontrado_lineal = busqueda_lineal(usuarios, user_id_buscado)
    usuario_encontrado_binario = busqueda_binaria(usuarios_ordenados, user_id_buscado)

    print(f"Resultado de búsqueda lineal: {usuario_encontrado_lineal}")
    print(f"Resultado de búsqueda binaria: {usuario_encontrado_binario}")
