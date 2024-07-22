# Clase 6: Introducción a Streamlit y Groq
import streamlit as st
from groq import Groq

# Configuración básica
MODELOS = ['llama3-8b-8192', 'llama3-70b-8192', 'mixtral-8x7b-32768']

def interfaz_basica():
    st.set_page_config(page_title="Mi chat de IA", page_icon="🤖")
    st.title("Mi chat de IA")
    st.sidebar.title("Configuración de la IA")
    modelo = st.sidebar.selectbox('Elegí un Modelo', options=MODELOS, index=0)
    return modelo


def obtener_clave_api():
    return st.secrets["groqApi"]

def crear_cliente_groq():
    return Groq(api_key='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')



# Clase 7: Configuración del modelo y variables de estado
def configurar_modelo(cliente, modelo, mensaje):
    return cliente.chat.completions.create(
        model=modelo,
        messages=[{"role": "user", "content": mensaje}],
        stream=True
    )

def inicializar_estado():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []

# Clase 8: Manejo de historiales de chat
def actualizar_historial(rol, contenido):
    st.session_state.mensajes.append({"role": rol, "content": contenido})

def mostrar_historial():
    for mensaje in st.session_state.mensajes:
        with st.chat_message(mensaje["role"]):
            st.markdown(mensaje["content"])

# Clase 9: Personalización del chatbot
def area_chat():
    # st.markdown("### Historial de Chat") # Puede estar como no. Es indistinto.
    chat_container = st.container()
    with chat_container:
        mostrar_historial()

def generar_respuesta(chat_completo):
    "rellena la cadena de caracteres"
    respuesta_completa = ""
    for chunk in chat_completo:
        if chunk.choices[0].delta.content:
            respuesta_completa += chunk.choices[0].delta.content
            yield chunk.choices[0].delta.content
    return respuesta_completa

def main():
    cliente = crear_cliente_groq()
    inicializar_estado()
    
    modelo = interfaz_basica()
    
    # Mostramos el historial del chat
    area_chat()
    
    # Campo de entrada para el mensaje al final de la página
    mensaje = st.chat_input("Escribí tu mensaje:")
    
    if mensaje:
        ## FALTA MODIFICAR EL TRY Y EXCEPT (no se ve en clase) PARA QUE SEA CON CONDICIONALES (se ve en clase).
        actualizar_historial("user", mensaje)
        chat_completo = configurar_modelo(cliente, modelo, mensaje)
        with st.chat_message("assistant"):
            respuesta_completa = st.write_stream(generar_respuesta(chat_completo))
        actualizar_historial("assistant", respuesta_completa)
        # Actualizamos la página para ver todos los estados, los nuevos y los viejos.
        st.rerun()

if __name__ == "__main__":
    main()
