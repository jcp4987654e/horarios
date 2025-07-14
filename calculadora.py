import streamlit as st
import streamlit.components.v1 as components
import os

# --- Configuración de la página de Streamlit ---
st.set_page_config(
    page_title="Mi Horario Interactivo",
    page_icon="🗓️",
    layout="wide"  # Usar el ancho completo de la página
)

st.title("🗓️ Visualizador de Horario Interactivo")
st.write("Esta aplicación muestra tu horario personal interactivo. Puedes editarlo, ponerlo en pantalla completa o exportarlo a PDF.")

# --- Cargar y mostrar el archivo HTML ---

# Define el nombre del archivo HTML
html_file_path = 'horario.html'

# Verifica si el archivo HTML existe en la misma carpeta
if os.path.exists(html_file_path):
    # Abrir y leer el archivo
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_code = f.read()
    
    # Usar st.components.v1.html para renderizar el código
    # Se recomienda un alto (height) generoso para evitar barras de desplazamiento dobles
    components.html(html_code, height=800, scrolling=True)
else:
    # Mensaje de error si no se encuentra el archivo
    st.error(f"Error: No se encontró el archivo '{html_file_path}'.")
    st.warning("Por favor, asegúrate de que el archivo HTML del horario esté en la misma carpeta que este script de Python y que se llame 'horario.html'.")
    st.info("Puedes obtener el código HTML del Canvas anterior.")

# --- Instrucciones de uso ---
st.sidebar.header("Instrucciones")
st.sidebar.markdown("""
1.  **Guarda el código** del Canvas anterior en un archivo llamado `horario.html`.
2.  **Guarda este código** de Python en un archivo (por ejemplo, `app.py`) en la **misma carpeta**.
3.  Abre una terminal o línea de comandos.
4.  Navega a la carpeta donde guardaste los archivos.
5.  Instala Streamlit si no lo has hecho:
    ```bash
    pip install streamlit
    ```
6.  Ejecuta la aplicación con el comando:
    ```bash
    streamlit run app.py
    ```
""")
