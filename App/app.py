import tkinter as tk
import json
from datetime import datetime
import random

# -----------------------------------------------------------------------------
# Constante año actual para derechos reservados ©
año_actual = datetime.today().year

# -----------------------------------------------------------------------------
# Configuraciones de colores
# -----------------------------------------------------------------------------
# Backgrounds
color_base_background_principal = "alice blue"
color_base_background_secundario = "light salmon"
color_base_boton = "white"

# -----------------------------------------------------------------------------
# Configuraciones de textos y widgets
# -----------------------------------------------------------------------------
# Propiedades principales
color_fuente_principal = "black"
propiedades_texto_titulo_principal = ("ComicSans", 25)
# Propiedades secundarias
color_fuente_secundaria = "white"
propiedades_texto_titulo_secundario = ("ComicSans", 10)
# Propiedades terciarias
color_fuente_terciarias = "black"
propiedades_texto_titulo_terciario = ("ComicSans", 8)
# Propiedades botones
color_fuente_boton = "black"
propiedades_texto_boton = ("Arial", 10)


# Obtención del json con los temas, preguntas y respuestas
def obtener_json():
    with open("preguntas_y_respuestas.json", "r", encoding="utf-8") as f:
        json_eval = json.load(f)
    return json_eval


json_autoevaluacion = obtener_json()

# -----------------------------------------------------------------------------
# Ventana principal
main_window = tk.Tk()
main_window.title("WBA - Plataforma de Autoevaluación")
main_window.geometry("800x600")
main_window.resizable(False, False)
main_window.configure(bg=color_base_background_principal)

titulo_ppl = tk.Label(
    main_window,
    text="WhiteBox Academy",
    bg=color_base_background_principal,
    fg=color_fuente_principal,
    font=propiedades_texto_titulo_principal,
)
titulo_ppl.pack()

separador = tk.Label(
    main_window,
    text="--------------------------------------------------------------------------------------------------------------",
    bg=color_base_background_principal,
    fg="salmon1",
    font=("Arial", 5),
)
separador.pack()

etiqueta_main_text = tk.Label(
    main_window,
    text="Bienvenid@ a la plataforma de autoevaluación. \nSelecciona un tema y mide tus conocimientos de Python.\n¡Tras realizar la pruba, recibirás tu nota!",
    bg=color_base_background_principal,
    fg=color_fuente_principal,
)
etiqueta_main_text.pack(pady=10)

label_frame = tk.LabelFrame(
    main_window,
    text="Selecciona un tema para iniciar el test de autoevaluación ",
    bg=color_base_background_secundario,
    fg=color_fuente_secundaria,
    font=propiedades_texto_titulo_secundario,
)

variable_control_tema = tk.IntVar()

for key, value in json_autoevaluacion.items():
    tema = tk.Radiobutton(
        label_frame,
        text="Tema " + key + " - " + value["nombre_tema"],
        bg=color_base_background_secundario,
        variable=variable_control_tema,
        font=("Arial", 10),
        value=int(key),
    )
    tema.pack(anchor="w")

label_frame.pack(pady=0, padx=15, fill="both", expand="yes")


def abrir_ventana_evaluacion():

    tema_seleccionado = variable_control_tema.get() 

    if tema_seleccionado == 0:
        test_error_window = tk.Toplevel(main_window)
        test_error_window.title("Error")
        test_error_window.geometry("500x140")
        test_error_window.resizable(False, False)
        test_error_window.configure(bg="indian red") # "light coral"
        etiqueta_error = tk.Label(
            test_error_window,
            text="¡Ups!\nNo has seleccionado ningún tema...\nCierra esta ventana y elige un tema\n~ Gracias ~",
            bg="indian red", # "light coral"
            fg="white",
            font=("Arial", 12),
        )
        etiqueta_error.pack(pady=10, padx=10)

        # Botón para cerrar la ventana de error
        boton_cerrar_ventana = tk.Button(test_error_window, 
                                         text=" Cerrar ventana ", 
                                         command=test_error_window.destroy, 
                                         font=("Arial", 10, "bold"),
                                         fg="black",)
        boton_cerrar_ventana.pack()

        test_error_window.mainloop()
    else:
        test_main_window = tk.Toplevel(main_window)
        test_main_window.title(f"WhiteBox Academy - Plataforma de Autoevaluación")
        test_main_window.geometry("800x900")
        test_main_window.resizable(False, False)
        test_main_window.configure(bg=color_base_background_principal)

        titulo_test_ppl = tk.Label(
            test_main_window,
            text="Autoevaluación",
            bg=color_base_background_principal,
            fg=color_fuente_principal,
            font=propiedades_texto_titulo_principal,
            )
        titulo_test_ppl.pack()
        
        separador_test = tk.Label(
            test_main_window,
            text="--------------------------------------------------------------------------------------------------------------",
            bg=color_base_background_principal,
            fg="green",
            font=("Arial", 5),
        )
        separador_test.pack()

        texto_test = tk.Label(
            test_main_window,
            text=f"Has seleccionado el Tema {tema_seleccionado} - {json_autoevaluacion[str(tema_seleccionado)]['nombre_tema']}\nCada pregunta solo tiene una respuesta correcta\nUsa el botón 'Obtener Resultado' para finalizar el test y conocer tu puntuación", 
            bg=color_base_background_principal,
            fg=color_fuente_principal,
        )
        texto_test.pack(pady=10)

        # LabelFrame Test
        label_frame_test = tk.LabelFrame(
            test_main_window,
            text="Test de autoevaluación",
            bg=color_base_background_secundario,
            fg=color_fuente_secundaria,
            font=propiedades_texto_titulo_secundario,
            )

        # Añadir lógica para devolver 3 preguntas aleatorias del tema seleccionado
        total_preguntas_por_tema = len(json_autoevaluacion[str(tema_seleccionado)]["preguntas"])
        num_preguntas_a_mostrar = 5
        numero_pregunta_aleatoria = random.sample(range(1, total_preguntas_por_tema), num_preguntas_a_mostrar)

        separador_test = tk.Label(
            label_frame_test,
            text="--------------------------------------------------------------------------------------------------------------",
            bg=color_base_background_secundario,
            fg="black",
            font=("Arial", 5),
        )

        # ---------------------------------------------------------------------------- #
        # Conjunto de preguntas aleatorias seleccionadas para el test
        # Pregunta 1:
        identificador_pregunta_1 = numero_pregunta_aleatoria[0]
        pregunta_1 = json_autoevaluacion[str(tema_seleccionado)]["preguntas"][identificador_pregunta_1]
        texto_pregunta_1 = list(pregunta_1.values())[0]
        label_pregunta_1 = tk.Label(
            label_frame_test,
            text=f" 1. {texto_pregunta_1}",
            bg=color_base_background_secundario,
            fg=color_fuente_principal,
            font=("Arial", 10, "bold"),
        )
        label_pregunta_1.pack(anchor="w", pady=5)

        respuestas_1 = pregunta_1["respuestas"]
        variable_control_respuesta_1 = tk.IntVar()
        for idx, respuesta in enumerate(respuestas_1):
            texto_respuesta = respuesta["texto"]
            radio_respuesta = tk.Radiobutton(
                label_frame_test,
                text=texto_respuesta,
                bg=color_base_background_secundario,
                variable=variable_control_respuesta_1,
                value=idx,
            )
            radio_respuesta.pack(anchor="w")
        
        # Pregunta 2:
        identificador_pregunta_2 = numero_pregunta_aleatoria[1]
        pregunta_2 = json_autoevaluacion[str(tema_seleccionado)]["preguntas"][identificador_pregunta_2]
        texto_pregunta_2 = list(pregunta_2.values())[0]
        label_pregunta_2 = tk.Label(
            label_frame_test,
            text=f" 2. {texto_pregunta_2}",
            bg=color_base_background_secundario,
            fg=color_fuente_principal,
            font=("Arial", 10, "bold"),
        )
        label_pregunta_2.pack(anchor="w", pady=5)

        respuestas_2 = pregunta_2["respuestas"]
        variable_control_respuesta_2 = tk.IntVar()
        for idx, respuesta in enumerate(respuestas_2):
            texto_respuesta = respuesta["texto"]
            radio_respuesta = tk.Radiobutton(
                label_frame_test,
                text=texto_respuesta,
                bg=color_base_background_secundario,
                variable=variable_control_respuesta_2,
                value=idx,
            )
            radio_respuesta.pack(anchor="w")

        # Pregunta 3:
        identificador_pregunta_3 = numero_pregunta_aleatoria[2]
        pregunta_3 = json_autoevaluacion[str(tema_seleccionado)]["preguntas"][identificador_pregunta_3]
        texto_pregunta_3 = list(pregunta_3.values())[0]
        label_pregunta_3 = tk.Label(
            label_frame_test,
            text=f" 3. {texto_pregunta_3}",
            bg=color_base_background_secundario,
            fg=color_fuente_principal,
            font=("Arial", 10, "bold"),
        )
        label_pregunta_3.pack(anchor="w", pady=5)

        respuestas_3 = pregunta_3["respuestas"]
        variable_control_respuesta_3 = tk.IntVar()
        for idx, respuesta in enumerate(respuestas_3):
            texto_respuesta = respuesta["texto"]
            radio_respuesta = tk.Radiobutton(
                label_frame_test,
                text=texto_respuesta,
                bg=color_base_background_secundario,
                variable=variable_control_respuesta_3,
                value=idx,
            )
            radio_respuesta.pack(anchor="w")

        # Pregunta 4:
        identificador_pregunta_4 = numero_pregunta_aleatoria[3]
        pregunta_4 = json_autoevaluacion[str(tema_seleccionado)]["preguntas"][identificador_pregunta_4]
        texto_pregunta_4 = list(pregunta_4.values())[0]
        label_pregunta_4 = tk.Label(
            label_frame_test,
            text=f" 4. {texto_pregunta_4}",
            bg=color_base_background_secundario,
            fg=color_fuente_principal,
            font=("Arial", 10, "bold"),
        )
        label_pregunta_4.pack(anchor="w", pady=5)

        respuestas_4 = pregunta_4["respuestas"]
        variable_control_respuesta_4 = tk.IntVar()
        for idx, respuesta in enumerate(respuestas_4):
            texto_respuesta = respuesta["texto"]
            radio_respuesta = tk.Radiobutton(
                label_frame_test,
                text=texto_respuesta,
                bg=color_base_background_secundario,
                variable=variable_control_respuesta_4,
                value=idx,
            )
            radio_respuesta.pack(anchor="w")

        # Pregunta 5:
        identificador_pregunta_5 = numero_pregunta_aleatoria[4]
        pregunta_5 = json_autoevaluacion[str(tema_seleccionado)]["preguntas"][identificador_pregunta_5]
        texto_pregunta_5 = list(pregunta_5.values())[0]
        label_pregunta_5 = tk.Label(
            label_frame_test,
            text=f" 5. {texto_pregunta_5}",
            bg=color_base_background_secundario,
            fg=color_fuente_principal,
            font=("Arial", 10, "bold"),
        )
        label_pregunta_5.pack(anchor="w", pady=5)

        respuestas_5 = pregunta_5["respuestas"]
        variable_control_respuesta_5 = tk.IntVar()
        for idx, respuesta in enumerate(respuestas_5):
            texto_respuesta = respuesta["texto"]
            radio_respuesta = tk.Radiobutton(
                label_frame_test,
                text=texto_respuesta,
                bg=color_base_background_secundario,
                variable=variable_control_respuesta_5,
                value=idx,
            )
            radio_respuesta.pack(anchor="w")

        # Fin conjunto preguntas aleatorias
        # ---------------------------------------------------------------------------- #

        def obtener_nota_evaluacion():

            # Se obtiene la posición de la respuesta seleccionada y nos ayudará a optener el valor de la respuesta
            # Se multiplica por 2 para poder dar la nota sobre 10 puntos
            posicion_respuesta_1 = variable_control_respuesta_1.get()
            posicion_respuesta_2 = variable_control_respuesta_2.get()
            posicion_respuesta_3 = variable_control_respuesta_3.get()
            posicion_respuesta_4 = variable_control_respuesta_4.get()
            posicion_respuesta_5 = variable_control_respuesta_5.get()

            valor_r1 = json_autoevaluacion[str(tema_seleccionado)]["preguntas"][identificador_pregunta_1]["respuestas"][posicion_respuesta_1]["correcta"]
            valor_r2 = json_autoevaluacion[str(tema_seleccionado)]["preguntas"][identificador_pregunta_2]["respuestas"][posicion_respuesta_2]["correcta"]
            valor_r3 = json_autoevaluacion[str(tema_seleccionado)]["preguntas"][identificador_pregunta_3]["respuestas"][posicion_respuesta_3]["correcta"]
            valor_r4 = json_autoevaluacion[str(tema_seleccionado)]["preguntas"][identificador_pregunta_4]["respuestas"][posicion_respuesta_4]["correcta"]
            valor_r5 = json_autoevaluacion[str(tema_seleccionado)]["preguntas"][identificador_pregunta_5]["respuestas"][posicion_respuesta_5]["correcta"]
            nota = (valor_r1 + valor_r2 + valor_r3 + valor_r4 + valor_r5) * 2
            # Evaluación Pregunta 1
            if nota < 5:
                texto = "Te recomiendo seguir practicando, ¡tú puedes!"
            elif 5 <= nota < 8:
                texto = "¡Buen trabajo! Sigue así."
            else:
                texto = "¡Excelente! Has dominado el tema."
            

            resultado_window = tk.Toplevel(test_main_window)
            resultado_window.title("Resultado del Test de Autoevaluación")
            resultado_window.geometry("400x150")
            resultado_window.resizable(False, False)
            resultado_window.configure(bg="light blue")
            etiqueta_resultado = tk.Label(
                resultado_window,
                text=f"¡Has finalizado el test!\nTu puntuación es: {nota} / 10\n{texto}",
                bg="light blue",
                fg="black",
                font=("Arial", 12, "bold"),
            )
            etiqueta_resultado.pack(pady=20)
            resultado_window.mainloop()

        # Botón para iniciar el test de autoevaluación
        boton_dar_evaluacion = tk.Button(
            label_frame_test,
            text="Obtener Resultado",
            fg=color_fuente_boton,
            bg=color_base_boton,
            font=propiedades_texto_boton,
            command=obtener_nota_evaluacion,
            )
        boton_dar_evaluacion.pack(side="bottom", pady=10)

        label_frame_test.pack(pady=0, 
                              padx=15, 
                              fill="both", 
                              expand="yes")
        

        etiqueta_derechos = tk.Label(
            test_main_window,
            text=f"© {año_actual} WhiteBox Academy. Todos los derechos reservados.",
            bg=color_base_background_principal,
            fg=color_fuente_terciarias,
            font=propiedades_texto_titulo_terciario,
            )

        etiqueta_derechos.pack(side="bottom", pady=10)

        test_main_window.mainloop()

# Botón para iniciar el test de autoevaluación
boton_crear_test = tk.Button(
    label_frame,
    text="Iniciar Test",
    fg=color_fuente_boton,
    bg=color_base_boton,
    font=propiedades_texto_boton,
    command=abrir_ventana_evaluacion,
)
boton_crear_test.pack(side="bottom", pady=10)

# -----------------------------------------------------------------------------
# Derechos reservados
etiqueta_derechos = tk.Label(
    main_window,
    text=f"© {año_actual} WhiteBox Academy. Todos los derechos reservados.",
    bg=color_base_background_principal,
    fg=color_fuente_terciarias,
    font=propiedades_texto_titulo_terciario,
)

etiqueta_derechos.pack(side="bottom", pady=10)
# -----------------------------------------------------------------------------

main_window.mainloop()
