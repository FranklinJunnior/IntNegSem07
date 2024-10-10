# Definición de los datos de los usuarios y sus calificaciones
users = {
    "Angelica": {
        "Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5,
        "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5,
        "Vampire Weekend": 2.0
    },
    "Bill": {
        "Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0,
        "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0
    },
    "Chan": {
        "Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0,
        "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 1.0
    },
    "Dan": {
        "Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5,
        "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0,
        "Vampire Weekend": 2.0
    },
    "Hailey": {
        "Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0,
        "The Strokes": 4.0, "Vampire Weekend": 1.0
    },
    "Jordyn": {
        "Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0,
        "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0,
        "Vampire Weekend": 4.0
    },
    "Sam": {
        "Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0,
        "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0
    },
    "Veronica": {
        "Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0,
        "Slightly Stoopid": 2.5, "The Strokes": 3.0
    }
}

# Función para calcular la distancia de Manhattan entre dos usuarios
def manhattan(rating1, rating2):
    """Calcula la distancia de Manhattan. Ambos rating1 y rating2 son diccionarios."""
    distance = 0
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
    return distance

# Función para encontrar el vecino más cercano
def computeNearestNeighbor(username, users):
    """Crea una lista ordenada de usuarios basada en la distancia al username."""
    distances = []
    for user in users:
        if user != username:
            distance = manhattan(users[user], users[username])
            distances.append((distance, user))
    # Ordenar la lista de distancias, el vecino más cercano primero
    distances.sort()
    return distances

# Función para hacer recomendaciones basadas en el vecino más cercano
def recommend(username, users):
    """Devuelve una lista de recomendaciones de bandas para el username."""
    nearest = computeNearestNeighbor(username, users)[0][1]
    recommendations = []
    neighborRatings = users[nearest]
    userRatings = users[username]
    for artist in neighborRatings:
        if artist not in userRatings:
            recommendations.append((artist, neighborRatings[artist]))
    # Ordenar las recomendaciones en orden descendente
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse=True)

# Ejecución de las funciones para obtener recomendaciones para 'Hailey'
if __name__ == "__main__":
    print("Recomendaciones para Hailey:")
    print(recommend('Hailey', users))

    print("\nRecomendaciones para Chan:")
    print(recommend('Chan', users))
