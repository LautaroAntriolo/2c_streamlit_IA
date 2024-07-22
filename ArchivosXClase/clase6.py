import streamlit as st
from groq import Groq

# Configuración básica
MODELOS = ['llama3-8b-8192', 'llama3-70b-8192', 'mixtral-8x7b-32768']

def configurar_pagina():
    st.set_page_config(page_title="Mi chat de IA", page_icon="🤖")
    st.title("Mi chat de IA")
    st.write("Bienvenido a mi chat de IA")

def crear_cliente_groq():
    return Groq(api_key='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')

def obtener_clave_api():
    return st.secrets["groqApi"]

def interfaz_basica():
    st.sidebar.title("Configuración de la IA")
    modelo = st.sidebar.selectbox('Elegí un Modelo', options=MODELOS, index=0)
    return modelo