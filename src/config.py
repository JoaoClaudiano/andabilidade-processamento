# src/config.py

# Categorias e pesos (seguindo a lógica do Walk Score original)
CATEGORIES = {
    'amenity': {
        'restaurant': 0.75,
        'cafe': 0.5,
        'pharmacy': 1.0,
        'bank': 0.5,
        'school': 1.0,
        'hospital': 1.0,
        'clinic': 0.75
    },
    'shop': {
        'supermarket': 1.0,
        'bakery': 1.0,
        'convenience': 0.5,
        'mall': 0.5
    },
    'leisure': {
        'park': 1.0,
        'playground': 0.5
    }
}

# Distância máxima de caminhada (em metros)
MAX_WALK_DIST = 1600 # aprox. 20 minutos
