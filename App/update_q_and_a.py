import json

banco_preguntas_y_respuestas = {
    1: {  # Tema 1
        "nombre_tema": "Python Básico",
        "preguntas": [
            {
                1: "¿Qué tipo de dato devuelve la función len() en Python?",
                "respuestas": [
                    {"texto": "Entero", "correcta": 1},
                    {"texto": "Cadena de texto", "correcta": 0},
                    {"texto": "Booleano", "correcta": 0},
                    {"texto": "Lista", "correcta": 0},
                ],
            },
            {
                2: "¿Cuál de las siguientes opciones crea una lista vacía?",
                "respuestas": [
                    {"texto": "{}", "correcta": 0},
                    {"texto": "[]", "correcta": 1},
                    {"texto": "()", "correcta": 0},
                    {"texto": "None", "correcta": 0},
                ],
            },
            {
                3: "¿Qué palabra clave se utiliza para definir una función en Python?",
                "respuestas": [
                    {"texto": "function", "correcta": 0},
                    {"texto": "def", "correcta": 1},
                    {"texto": "fun", "correcta": 0},
                    {"texto": "lambda", "correcta": 0},
                ],
            },
            {
                4: "¿Cuál de las siguientes opciones es un tipo de dato inmutable en Python?",
                "respuestas": [
                    {"texto": "Lista", "correcta": 0},
                    {"texto": "Conjunto", "correcta": 0},
                    {"texto": "Tupla", "correcta": 1},
                    {"texto": "Diccionario", "correcta": 0},
                ],
            },
            {
                5: "¿Qué operador se utiliza para comparar igualdad en Python?",
                "respuestas": [
                    {"texto": "=", "correcta": 0},
                    {"texto": "==", "correcta": 1},
                    {"texto": "===", "correcta": 0},
                    {"texto": "!=", "correcta": 0},
                ],
            },
            {
                6: "¿Qué devuelve la expresión bool(0) en Python?",
                "respuestas": [
                    {"texto": "True", "correcta": 0},
                    {"texto": "False", "correcta": 1},
                    {"texto": "0", "correcta": 0},
                    {"texto": "None", "correcta": 0},
                ],
            },
            {
                7: "¿Cuál de las siguientes estructuras permite almacenar pares clave-valor?",
                "respuestas": [
                    {"texto": "Lista", "correcta": 0},
                    {"texto": "Tupla", "correcta": 0},
                    {"texto": "Diccionario", "correcta": 1},
                    {"texto": "Conjunto", "correcta": 0},
                ],
            },
            {
                8: "¿Qué función se utiliza para obtener la entrada del usuario en Python?",
                "respuestas": [
                    {"texto": "read()", "correcta": 0},
                    {"texto": "input()", "correcta": 1},
                    {"texto": "scan()", "correcta": 0},
                    {"texto": "get()", "correcta": 0},
                ],
            },
            {
                9: "¿Cuál es el resultado de la operación 3 * 'a' en Python?",
                "respuestas": [
                    {"texto": "'aaa'", "correcta": 1},
                    {"texto": "'a3'", "correcta": 0},
                    {"texto": "Error", "correcta": 0},
                    {"texto": "['a', 'a', 'a']", "correcta": 0},
                ],
            },
            {
                10: "¿Qué palabra clave se usa para manejar excepciones en Python?",
                "respuestas": [
                    {"texto": "error", "correcta": 0},
                    {"texto": "try", "correcta": 1},
                    {"texto": "catch", "correcta": 0},
                    {"texto": "except", "correcta": 0},
                ],
            },
        ],
    },
    2: {  # Tema 2
        "nombre_tema": "SQL",
        "preguntas": [
            {
                1: "¿Qué comando se usa para seleccionar datos de una tabla?",
                "respuestas": [
                    {"texto": "SELECT", "correcta": 1},
                    {"texto": "INSERT", "correcta": 0},
                    {"texto": "UPDATE", "correcta": 0},
                    {"texto": "DELETE", "correcta": 0},
                ],
            },
            {
                2: "¿Qué cláusula se usa para filtrar resultados?",
                "respuestas": [
                    {"texto": "GROUP BY", "correcta": 0},
                    {"texto": "WHERE", "correcta": 1},
                    {"texto": "ORDER BY", "correcta": 0},
                    {"texto": "FROM", "correcta": 0},
                ],
            },
        ],
    },
    3: {  # Tema 3
        "nombre_tema": "Estadística",
        "preguntas": [
            {
                1: "¿Cuál es la media de los números 2, 4 y 6?",
                "respuestas": [
                    {"texto": "3", "correcta": 0},
                    {"texto": "4", "correcta": 1},
                    {"texto": "5", "correcta": 0},
                    {"texto": "6", "correcta": 0},
                ],
            },
            {
                2: "¿Qué mide la desviación estándar?",
                "respuestas": [
                    {
                        "texto": "El valor más alto de un conjunto de datos",
                        "correcta": 0,
                    },
                    {
                        "texto": "La dispersión de los datos respecto a la media",
                        "correcta": 1,
                    },
                    {"texto": "La suma de todos los valores", "correcta": 0},
                    {"texto": "El número de observaciones", "correcta": 0},
                ],
            },
        ],
    },
}


with open("preguntas_y_respuestas.json", "w", encoding="utf-8") as f:
    json.dump(banco_preguntas_y_respuestas, f, indent=4, ensure_ascii=False)
print("JSON actualizado")
